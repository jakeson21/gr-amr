#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Jacob Miller.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr
from scipy import signal
import pmt

class symbols_to_bits(gr.sync_block):
    """
    docstring Takes messages with NRZ samples and converts to bits
    """
    def __init__(self, samps_per_bit, threshold):
        gr.sync_block.__init__(self,
            name="symbols_to_bits",
            in_sig=[],
            out_sig=None)
        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern("in"), self.handle_msg)
        self.message_port_register_out(pmt.intern('bits'))
        self._spb = samps_per_bit
        self._b = np.ones((int(np.floor(self._spb/2)*2),))
        self._b[int(len(self._b)/2):] = -1
        self._b = self._b / len(self._b)
        self._threshold = threshold


    def demodulate(self, input):
        xf = signal.lfilter(self._b, 1., input)
        # Hysteresis detector
        hys = np.zeros(xf.size)
        hys_pos = xf>self._threshold
        hys_neg = xf<-self._threshold
        state = 0
        n = 0
        for up, dn in zip(hys_pos, hys_neg):
            if up:
                hys[n] = 1
            elif dn:
                hys[n] = -1
            elif n>0:
                hys[n] = hys[n-1]
            n += 1
        start = np.argmax(np.abs(hys))
        bits = hys[start+1::self._spb]
        return (bits>0, start)


    def handle_msg(self, msg):
        # name = pmt.pmt_python.pmt_base()
        samples = pmt.pmt_python.pmt_base()
        if pmt.is_dict(msg):
            samples = pmt.dict_ref(msg, pmt.intern("samples"), pmt.PMT_NIL)
        elif pmt.is_pair(msg):
            # name = pmt.car(msg)
            samples = pmt.cdr(msg)
        elif pmt.is_uniform_vector(msg):
            samples = msg
        else:
            print('Unexpected pmt data format')
            return
        try:
            data = pmt.f32vector_elements(samples)
            bits, index = self.demodulate(data)
            self.message_port_pub(pmt.intern('bits'), pmt.cons(pmt.intern("bits"), pmt.init_f32vector(len(bits), bits)))
        except ValueError:
            print('Invalid value for samples')


    def work(self, input_items, output_items):
        return len(input_items[0])

