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
    def __init__(self, samps_per_bit, threshold, bit_rate):
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
        self._bit_rate = bit_rate


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
        # samples = pmt.pmt_python.pmt_base()
        # timestamp = pmt.pmt_python.pmt_base()
        # if pmt.is_dict(msg):
        #     samples = pmt.dict_ref(msg, pmt.intern("samples"), pmt.PMT_NIL)
        # elif pmt.is_pair(msg):
        #     samples = pmt.car(msg)
        # elif pmt.is_uniform_vector(msg):
        #     samples = msg
        meta = pmt.car(msg)
        if pmt.is_dict(meta) and pmt.dict_has_key(meta, pmt.intern("samples")):
            samples = pmt.dict_ref(meta, pmt.intern("samples"), pmt.PMT_NIL)
            timestamp = pmt.dict_ref(meta, pmt.intern("time"), pmt.PMT_NIL)
            timestamp = pmt.to_double(timestamp)
        else:
            print('Unexpected pmt data format')
            return
        try:
            data = pmt.f32vector_elements(samples)
            bits, index = self.demodulate(data)
            dt = index/(self._bit_rate * self._spb)
            meta = pmt.make_dict()
            meta = pmt.dict_add(meta, pmt.intern("bits"), pmt.init_f32vector(len(bits), bits))
            meta = pmt.dict_add(meta, pmt.intern("timestamp"), pmt.from_double(timestamp + dt))
            self.message_port_pub(pmt.intern('bits'), pmt.cons(meta, pmt.PMT_NIL))
        except ValueError:
            print('Invalid value for samples')


    def work(self, input_items, output_items):
        return len(input_items[0])

