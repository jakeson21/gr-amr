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

class packet_detector(gr.sync_block):
    """
    Takes in thresholded samples and detect and extracts the AMR packet bits
    """
    def __init__(self, sample_rate=200.0e3):
        gr.sync_block.__init__(self,
            name="packet_detector",
            in_sig=[np.float32],
            out_sig=None)
        
        self.message_port_register_out(pmt.intern('pdu'))
        self._samps_to_collect = int(np.floor(0.012 * sample_rate))
        self._samp_buffer = np.zeros((self._samps_to_collect,), dtype=np.uint8)
        self._samps_collected = 0
        self._state = 0 # 0=searching, 1=found-on


    def work(self, input_items, output_items):
        in0 = input_items[0]    
        # print('{} in0[0] = {}\n'.format(len(in0), in0[0]))
        # Detect AMR signal
        rising = 0
        if self._state == 0:
            rising = np.argmax(in0)
            if rising==0 and in0[0] == 0:
                # no 'on' bits found
                self._state = 0
            else:
                self._state = 1

        if self._state == 1:
            # grab _samps_to_collect if possible
            # calc last available index
            last = np.minimum(len(in0), rising+self._samps_to_collect-self._samps_collected) - 1
            # count samples to grab
            n_samps = last - rising + 1
            self._samp_buffer[self._samps_collected:self._samps_collected + n_samps - 1] = in0[rising:last].astype(dtype=np.uint8)
            self._samps_collected += n_samps
            # print('_samps_collected = {}\n'.format(self._samps_collected))

            if self._samps_collected >= self._samps_to_collect:
                self._state = 0
                self._samps_collected = 0
                data = pmt.make_dict()
                # key0 = pmt.intern("start_index")
                # val0 = pmt.from_double(np.sum(self._samp_buffer>0))
                # data = pmt.dict_add(data, key0, val0)
                key1 = pmt.intern("bits")
                val1 = pmt.init_u8vector(len(self._samp_buffer), self._samp_buffer)
                data = pmt.dict_add(data, key1, val1)
                pdu = pmt.cons(pmt.intern("packet"), data)
                self.message_port_pub(pmt.intern('pdu'), pdu)

        return len(in0)
