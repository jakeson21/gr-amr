#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Jacob Miller.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr
import pmt
import pdb
import matplotlib.pyplot as plt

class fsk_demod_ff(gr.sync_block):
    """
    docstring for block fsk_demod_ff
    """
    def __init__(self, center_freq, samp_rate, period):
        gr.sync_block.__init__(self,
            name="fsk_demod_ff",
            in_sig=[np.float32, np.float32],
            out_sig=None
            )
        self.message_port_register_out(pmt.intern('pdu'))
        self.set_output_multiple(2)
        self._center_freq = center_freq
        self._samp_rate = samp_rate
        self._samps_to_collect = int(np.floor(period * samp_rate))
        self._samp_buffer = np.zeros((self._samps_to_collect,), dtype=np.float32)
        self._samps_collected = 0
        self._state = 0 # 0=searching, 1=collecting


    def work(self, input_items, output_items):
        in0 = input_items[0]
        detected = input_items[1]
        # <+signal processing here+>

        # Assume the first rising edge is the start of a packet, and only 1 packet exists in input
        rising = np.argmax(detected)
        samps_available = len(in0) - rising
        if (rising > 0) or (self._state == 1) or (rising == 0 and detected[0] > 0):
            if self._state == 0 and samps_available >= self._samps_to_collect: # all samples are available now
                data = np.unwrap(in0[rising:rising+self._samps_to_collect-1])
                data = data - (np.amax(data[:int(self._samps_to_collect/2)]) + np.amin(data[:int(self._samps_to_collect/2)])) / 2.
                self.message_port_pub(pmt.intern('pdu'), pmt.cons(pmt.intern("samples"), pmt.init_f32vector(self._samps_to_collect, data)))
            elif self._state == 0: # samples are split between calls, first pass through
                length = samps_available
                self._samp_buffer[self._samps_collected:self._samps_collected+length-1] = in0[rising:rising+length-1]
                self._samps_collected += length
                # need more samples
                self._state = 1
            else:
                length = np.minimum(self._samps_to_collect-self._samps_collected, len(in0))
                self._samp_buffer[self._samps_collected:self._samps_collected+length-1] = in0[:length-1]
                self._samps_collected += length
                if self._samps_collected >= self._samps_to_collect:
                    data = np.unwrap(self._samp_buffer)
                    data = data - (np.amax(data[:int(self._samps_to_collect/2)]) + np.amin(data[:int(self._samps_to_collect/2)])) / 2.
                    self.message_port_pub(pmt.intern('pdu'), pmt.cons(pmt.intern("samples"), pmt.init_f32vector(self._samps_to_collect, data)))
                    self._samp_buffer = np.zeros((self._samps_to_collect,), dtype=np.float32)
                    self._state = 0
                    self._samps_collected = 0
                else: 
                    # need more samples
                    self._state = 1

        return len(input_items[0])

