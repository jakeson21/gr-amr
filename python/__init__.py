#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio AMR module. Place your Python package
description here (python/__init__.py).
'''
import os

# import pybind11 generated symbols into the amr namespace
try:
    # this might fail if the module is python-only
    from .amr_python import *
except ModuleNotFoundError:
    pass

# import any pure python here
from .packet_detector import packet_detector
from .fsk_demod_ff import fsk_demod_ff
from .symbols_to_bits import symbols_to_bits
#
