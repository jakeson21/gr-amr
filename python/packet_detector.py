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
        #self.message_port_register_out(pmt.intern('out'))


    def work(self, input_items, output_items):
        in0 = input_items[0]
        #print(in0)
        # Detect AMR signal
        if np.any(in0>0):
            data = pmt.to_pmt(in0)
            meta = pmt.to_pmt('out')
            pdu = pmt.cons(meta, data)
            #print(pdu)
            # self.message_port_pub(pmt.intern('out'), pdu)

        return len(in0)
