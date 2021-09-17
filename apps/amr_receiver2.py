#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Amr Receiver2
# GNU Radio version: 3.9.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from amr_rx_heir import amr_rx_heir  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import numpy as np
import tools



from gnuradio import qtgui

class amr_receiver2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Amr Receiver2", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Amr Receiver2")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "amr_receiver2")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_Fc = variable_qtgui_Fc = 905.5895
        self.variable_qtgui_Gain = variable_qtgui_Gain = 40
        self.samp_rate_2 = samp_rate_2 = 100e3*24/25
        self.samp_rate = samp_rate = 100e3
        self.phase_trigger_level = phase_trigger_level = 0.2
        self.mag_trigger_level = mag_trigger_level = -15
        self.center_freq = center_freq = variable_qtgui_Fc*1e6
        self.N = N = 2

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_Gain_range = Range(0, 60, 1, 40, 200)
        self._variable_qtgui_Gain_win = RangeWidget(self._variable_qtgui_Gain_range, self.set_variable_qtgui_Gain, 'Gain', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._variable_qtgui_Gain_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._mag_trigger_level_range = Range(-60, 0, 1, -15, 200)
        self._mag_trigger_level_win = RangeWidget(self._mag_trigger_level_range, self.set_mag_trigger_level, 'Mag Trigger Level', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._mag_trigger_level_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_Fc_range = Range(905.5895, 905.5895 + 0.3618*52, 0.3618, 905.5895, 200)
        self._variable_qtgui_Fc_win = RangeWidget(self._variable_qtgui_Fc_range, self.set_variable_qtgui_Fc, 'Center Frequency (kHz)', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._variable_qtgui_Fc_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
            ",".join(("serial=3102419", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(center_freq, 50000.0), 0)
        self.uhd_usrp_source_1.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_1.set_bandwidth(samp_rate*N, 0)
        self.uhd_usrp_source_1.set_rx_agc(False, 0)
        self.uhd_usrp_source_1.set_gain(variable_qtgui_Gain, 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source_1.set_min_output_buffer(1000)
        self.tools_print_float_0 = tools.print_float('time', True)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=24,
                decimation=25,
                taps=[],
                fractional_bw=0)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            512, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.01)
        self.qtgui_waterfall_sink_x_0.enable_grid(True)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, -20)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            1024, #size
            9600, #samp_rate
            "Bits", #name
            0, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-0.5, 1.5)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(True)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)

        self.qtgui_time_sink_x_1_0.disable_legend()

        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_win)
        self._phase_trigger_level_range = Range(0, 1, 0.01, 0.2, 200)
        self._phase_trigger_level_win = RangeWidget(self._phase_trigger_level_range, self.set_phase_trigger_level, 'Phase Trigger Level', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._phase_trigger_level_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(100)
        self.blocks_msg_meta_to_pair_0_0 = blocks.meta_to_pair('timestamp','time')
        self.blocks_msg_meta_to_pair_0 = blocks.meta_to_pair('bits','bits')
        self.amr_rx_heir_0 = amr_rx_heir(
            bits_per_second=9600,
            center_freq=center_freq,
            mag_trigger_level=-15,
            period=0.0125,
            samp_rate=samp_rate_2,
        )



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.amr_rx_heir_0, 'bits'), (self.blocks_msg_meta_to_pair_0, 'inmeta'))
        self.msg_connect((self.amr_rx_heir_0, 'bits'), (self.blocks_msg_meta_to_pair_0_0, 'inmeta'))
        self.msg_connect((self.blocks_msg_meta_to_pair_0, 'outpair'), (self.qtgui_time_sink_x_1_0, 'in'))
        self.msg_connect((self.blocks_msg_meta_to_pair_0_0, 'outpair'), (self.tools_print_float_0, 'msg'))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.amr_rx_heir_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_multiply_const_vxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "amr_receiver2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_Fc(self):
        return self.variable_qtgui_Fc

    def set_variable_qtgui_Fc(self, variable_qtgui_Fc):
        self.variable_qtgui_Fc = variable_qtgui_Fc
        self.set_center_freq(self.variable_qtgui_Fc*1e6)

    def get_variable_qtgui_Gain(self):
        return self.variable_qtgui_Gain

    def set_variable_qtgui_Gain(self, variable_qtgui_Gain):
        self.variable_qtgui_Gain = variable_qtgui_Gain
        self.uhd_usrp_source_1.set_gain(self.variable_qtgui_Gain, 0)

    def get_samp_rate_2(self):
        return self.samp_rate_2

    def set_samp_rate_2(self, samp_rate_2):
        self.samp_rate_2 = samp_rate_2
        self.amr_rx_heir_0.set_samp_rate(self.samp_rate_2)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_1.set_bandwidth(self.samp_rate*self.N, 0)

    def get_phase_trigger_level(self):
        return self.phase_trigger_level

    def set_phase_trigger_level(self, phase_trigger_level):
        self.phase_trigger_level = phase_trigger_level

    def get_mag_trigger_level(self):
        return self.mag_trigger_level

    def set_mag_trigger_level(self, mag_trigger_level):
        self.mag_trigger_level = mag_trigger_level

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.amr_rx_heir_0.set_center_freq(self.center_freq)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.center_freq, 50000.0), 0)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.uhd_usrp_source_1.set_bandwidth(self.samp_rate*self.N, 0)




def main(top_block_cls=amr_receiver2, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
