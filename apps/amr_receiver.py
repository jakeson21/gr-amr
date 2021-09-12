#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Amr Receiver
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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import amr
import numpy as np



from gnuradio import qtgui

class amr_receiver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Amr Receiver", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Amr Receiver")
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

        self.settings = Qt.QSettings("GNU Radio", "amr_receiver")

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
        self.variable_qtgui_Fc = variable_qtgui_Fc = 908.122
        self.variable_trigger_level = variable_trigger_level = -17
        self.variable_qtgui_Gain = variable_qtgui_Gain = 40
        self.samp_rate = samp_rate = 200e3
        self.center_freq = center_freq = variable_qtgui_Fc*1e6
        self.N = N = 4

        ##################################################
        # Blocks
        ##################################################
        self._variable_trigger_level_range = Range(-80, 20, 1, -17, 200)
        self._variable_trigger_level_win = RangeWidget(self._variable_trigger_level_range, self.set_variable_trigger_level, 'Trigger Level', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_trigger_level_win)
        self._variable_qtgui_Gain_range = Range(0, 60, 1, 40, 200)
        self._variable_qtgui_Gain_win = RangeWidget(self._variable_qtgui_Gain_range, self.set_variable_qtgui_Gain, 'Gain', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_qtgui_Gain_win)
        self._variable_qtgui_Fc_range = Range(89, 930, 0.001, 908.122, 200)
        self._variable_qtgui_Fc_win = RangeWidget(self._variable_qtgui_Fc_range, self.set_variable_qtgui_Fc, 'Center Frequency (kHz)', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_qtgui_Fc_win)
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

        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(center_freq, samp_rate), 0)
        self.uhd_usrp_source_1.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_1.set_bandwidth(samp_rate*N, 0)
        self.uhd_usrp_source_1.set_rx_agc(False, 0)
        self.uhd_usrp_source_1.set_gain(variable_qtgui_Gain, 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            2048, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            center_freq*0., #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.02)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, -50)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, [-1.32218580e-03+0.00000000e+00j,-7.69165817e-04-1.13774280e-03j, 4.70769845e-04-1.40938578e-03j, 1.45596554e-03-6.07222859e-04j, 1.43932680e-03+6.51552628e-04j, 4.54243736e-04+1.38988501e-03j,-6.88762261e-04+1.03642492e-03j,-1.02692028e-03-9.36586647e-05j,-2.33724984e-04-1.00954137e-03j, 1.06157602e-03-8.30543590e-04j, 1.73035887e-03+4.57077541e-04j, 1.06213804e-03+1.91303497e-03j,-5.96231096e-04+2.36029493e-03j,-2.05219301e-03+1.36242280e-03j,-2.21861069e-03-3.59687047e-04j,-1.03895412e-03-1.47611117e-03j, 4.18726998e-04-1.15497672e-03j, 8.36788075e-04+1.98192844e-04j,-2.10610604e-04+1.23722543e-03j,-1.83075585e-03+8.10663236e-04j,-2.51321844e-03-1.00764763e-03j,-1.40882521e-03-2.89545488e-03j, 8.92553091e-04-3.33731076e-03j, 2.77918097e-03-1.89880747e-03j, 2.92302465e-03+3.62798096e-04j, 1.39564324e-03+1.73533941e-03j,-3.59490096e-04+1.27184419e-03j,-7.16731803e-04-3.85542794e-04j, 7.38267059e-04-1.49577062e-03j, 2.77481686e-03-6.67484748e-04j, 3.45426380e-03+1.90210175e-03j, 1.73134007e-03+4.44608978e-03j,-1.57337859e-03+4.96917784e-03j,-4.28467597e-03+2.88929715e-03j,-4.55991569e-03-3.63942883e-04j,-2.44600733e-03-2.38632865e-03j, 1.64928756e-05-1.75971039e-03j, 3.89346582e-04+6.27596593e-04j,-2.03082307e-03+2.11204679e-03j,-5.32324505e-03+4.24726467e-04j,-6.25881875e-03-4.16569024e-03j,-2.99854987e-03-8.63979857e-03j, 3.01045726e-03-9.44930274e-03j, 7.78286001e-03-5.58336909e-03j, 7.96186700e-03+1.56468553e-04j, 3.93161125e-03+3.15032311e-03j,-3.20525468e-06+9.64784294e-04j, 9.30782071e-04-3.98761294e-03j, 7.44555543e-03-5.87250197e-03j, 1.46365764e-02-3.81840642e-04j, 1.54486273e-02+1.07720365e-02j, 6.88600235e-03+2.01480276e-02j,-6.34411402e-03+2.03385407e-02j,-1.47154144e-02+1.08790185e-02j,-1.19309075e-02+2.90007995e-05j,-1.66908389e-03-1.34604348e-03j, 3.56951908e-03+1.01905352e-02j,-7.76689808e-03+2.50976789e-02j,-3.48175601e-02+2.58663689e-02j,-6.09595053e-02+5.08625191e-04j,-6.32023902e-02-4.52982575e-02j,-2.89958991e-02-8.78167665e-02j, 3.18128552e-02-9.89654395e-02j, 8.98939539e-02-6.55263475e-02j, 1.13740378e-01+0.00000000e+00j, 8.98939539e-02+6.55263475e-02j, 3.18128552e-02+9.89654395e-02j,-2.89958991e-02+8.78167665e-02j,-6.32023902e-02+4.52982575e-02j,-6.09595053e-02-5.08625191e-04j,-3.48175601e-02-2.58663689e-02j,-7.76689808e-03-2.50976789e-02j, 3.56951908e-03-1.01905352e-02j,-1.66908389e-03+1.34604348e-03j,-1.19309075e-02-2.90007995e-05j,-1.47154144e-02-1.08790185e-02j,-6.34411402e-03-2.03385407e-02j, 6.88600235e-03-2.01480276e-02j, 1.54486273e-02-1.07720365e-02j, 1.46365764e-02+3.81840642e-04j, 7.44555543e-03+5.87250197e-03j, 9.30782071e-04+3.98761294e-03j,-3.20525468e-06-9.64784294e-04j, 3.93161125e-03-3.15032311e-03j, 7.96186700e-03-1.56468553e-04j, 7.78286001e-03+5.58336909e-03j, 3.01045726e-03+9.44930274e-03j,-2.99854987e-03+8.63979857e-03j,-6.25881875e-03+4.16569024e-03j,-5.32324505e-03-4.24726467e-04j,-2.03082307e-03-2.11204679e-03j, 3.89346582e-04-6.27596593e-04j, 1.64928756e-05+1.75971039e-03j,-2.44600733e-03+2.38632865e-03j,-4.55991569e-03+3.63942883e-04j,-4.28467597e-03-2.88929715e-03j,-1.57337859e-03-4.96917784e-03j, 1.73134007e-03-4.44608978e-03j, 3.45426380e-03-1.90210175e-03j, 2.77481686e-03+6.67484748e-04j, 7.38267059e-04+1.49577062e-03j,-7.16731803e-04+3.85542794e-04j,-3.59490096e-04-1.27184419e-03j, 1.39564324e-03-1.73533941e-03j, 2.92302465e-03-3.62798096e-04j, 2.77918097e-03+1.89880747e-03j, 8.92553091e-04+3.33731076e-03j,-1.40882521e-03+2.89545488e-03j,-2.51321844e-03+1.00764763e-03j,-1.83075585e-03-8.10663236e-04j,-2.10610604e-04-1.23722543e-03j, 8.36788075e-04-1.98192844e-04j, 4.18726998e-04+1.15497672e-03j,-1.03895412e-03+1.47611117e-03j,-2.21861069e-03+3.59687047e-04j,-2.05219301e-03-1.36242280e-03j,-5.96231096e-04-2.36029493e-03j, 1.06213804e-03-1.91303497e-03j, 1.73035887e-03-4.57077541e-04j, 1.06157602e-03+8.30543590e-04j,-2.33724984e-04+1.00954137e-03j,-1.02692028e-03+9.36586647e-05j,-6.88762261e-04-1.03642492e-03j, 4.54243736e-04-1.38988501e-03j, 1.43932680e-03-6.51552628e-04j, 1.45596554e-03+6.07222859e-04j, 4.70769845e-04+1.40938578e-03j,-7.69165817e-04+1.13774280e-03j], 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(variable_trigger_level-2.0, variable_trigger_level, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(20, 1, 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(100)
        self.blocks_message_debug_0 = blocks.message_debug(True)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.amr_packet_detector_0 = amr.packet_detector(samp_rate)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.amr_packet_detector_0, 'pdu'), (self.blocks_message_debug_0, 'print'))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.amr_packet_detector_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.fft_filter_xxx_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "amr_receiver")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_Fc(self):
        return self.variable_qtgui_Fc

    def set_variable_qtgui_Fc(self, variable_qtgui_Fc):
        self.variable_qtgui_Fc = variable_qtgui_Fc
        self.set_center_freq(self.variable_qtgui_Fc*1e6)

    def get_variable_trigger_level(self):
        return self.variable_trigger_level

    def set_variable_trigger_level(self, variable_trigger_level):
        self.variable_trigger_level = variable_trigger_level
        self.blocks_threshold_ff_0.set_hi(self.variable_trigger_level)
        self.blocks_threshold_ff_0.set_lo(self.variable_trigger_level-2.0)

    def get_variable_qtgui_Gain(self):
        return self.variable_qtgui_Gain

    def set_variable_qtgui_Gain(self, variable_qtgui_Gain):
        self.variable_qtgui_Gain = variable_qtgui_Gain
        self.uhd_usrp_source_1.set_gain(self.variable_qtgui_Gain, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq*0., self.samp_rate)
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.center_freq, self.samp_rate), 0)
        self.uhd_usrp_source_1.set_bandwidth(self.samp_rate*self.N, 0)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq*0., self.samp_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.center_freq, self.samp_rate), 0)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.uhd_usrp_source_1.set_bandwidth(self.samp_rate*self.N, 0)




def main(top_block_cls=amr_receiver, options=None):

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
