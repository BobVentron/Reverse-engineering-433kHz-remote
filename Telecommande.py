#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import iio
import Telecommande_epy_block_1_0 as epy_block_1_0  # embedded python block
import Telecommande_epy_block_1_0_0 as epy_block_1_0_0  # embedded python block
import Telecommande_epy_block_1_0_0_0 as epy_block_1_0_0_0  # embedded python block
import Telecommande_epy_block_1_0_1 as epy_block_1_0_1  # embedded python block
import Telecommande_epy_block_1_0_1_0 as epy_block_1_0_1_0  # embedded python block
import Telecommande_epy_block_1_0_2 as epy_block_1_0_2  # embedded python block
import Telecommande_epy_block_1_0_2_0 as epy_block_1_0_2_0  # embedded python block
import sip



class Telecommande(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
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

        self.settings = Qt.QSettings("GNU Radio", "Telecommande")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_recep = samp_rate_recep = 2000000
        self.samp_rate_envoye = samp_rate_envoye = 1000000
        self.on_off_recep = on_off_recep = 0
        self.on_off_envoye = on_off_envoye = 0
        self.envoye_bianire = envoye_bianire = 0
        self.entre_Binaire = entre_Binaire = (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1)
        self.copyrightMB = copyrightMB = '2024 Bermond Michel et Soleilhac Bastien'
        self.code_D = code_D = [1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0]
        self.code_C = code_C = [1,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0]
        self.code_B = code_B = [1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0]
        self.code_A_et_B_et_C_et_D = code_A_et_B_et_C_et_D = [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0]
        self.code_A_et_B_et_C = code_A_et_B_et_C = [1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0]
        self.address_telec = address_telec = [1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]
        self.Prémbule = Prémbule = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.Frequency = Frequency = 433920000
        self.D = D = 0
        self.Code_A_et_B = Code_A_et_B = [1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0]
        self.Code_A = Code_A = [1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0]
        self.C = C = 0
        self.B = B = 0
        self.A_et_B_et_C_et_D = A_et_B_et_C_et_D = 0
        self.A_et_B_et_C = A_et_B_et_C = 0
        self.A_et_B = A_et_B = 0
        self.A = A = 0

        ##################################################
        # Blocks
        ##################################################

        self.Tab_general = Qt.QTabWidget()
        self.Tab_general_widget_0 = Qt.QWidget()
        self.Tab_general_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_general_widget_0)
        self.Tab_general_grid_layout_0 = Qt.QGridLayout()
        self.Tab_general_layout_0.addLayout(self.Tab_general_grid_layout_0)
        self.Tab_general.addTab(self.Tab_general_widget_0, 'acceuil')
        self.Tab_general_widget_1 = Qt.QWidget()
        self.Tab_general_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_general_widget_1)
        self.Tab_general_grid_layout_1 = Qt.QGridLayout()
        self.Tab_general_layout_1.addLayout(self.Tab_general_grid_layout_1)
        self.Tab_general.addTab(self.Tab_general_widget_1, 'envoye')
        self.Tab_general_widget_2 = Qt.QWidget()
        self.Tab_general_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_general_widget_2)
        self.Tab_general_grid_layout_2 = Qt.QGridLayout()
        self.Tab_general_layout_2.addLayout(self.Tab_general_grid_layout_2)
        self.Tab_general.addTab(self.Tab_general_widget_2, 'récéption')
        self.top_grid_layout.addWidget(self.Tab_general, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.Tab_recep = Qt.QTabWidget()
        self.Tab_recep_widget_0 = Qt.QWidget()
        self.Tab_recep_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_recep_widget_0)
        self.Tab_recep_grid_layout_0 = Qt.QGridLayout()
        self.Tab_recep_layout_0.addLayout(self.Tab_recep_grid_layout_0)
        self.Tab_recep.addTab(self.Tab_recep_widget_0, 'demod')
        self.Tab_general_layout_2.addWidget(self.Tab_recep)
        self.Tab_envoye = Qt.QTabWidget()
        self.Tab_envoye_widget_0 = Qt.QWidget()
        self.Tab_envoye_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_envoye_widget_0)
        self.Tab_envoye_grid_layout_0 = Qt.QGridLayout()
        self.Tab_envoye_layout_0.addLayout(self.Tab_envoye_grid_layout_0)
        self.Tab_envoye.addTab(self.Tab_envoye_widget_0, 'Info')
        self.Tab_envoye_widget_1 = Qt.QWidget()
        self.Tab_envoye_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_envoye_widget_1)
        self.Tab_envoye_grid_layout_1 = Qt.QGridLayout()
        self.Tab_envoye_layout_1.addLayout(self.Tab_envoye_grid_layout_1)
        self.Tab_envoye.addTab(self.Tab_envoye_widget_1, 'Simu_Telecomande')
        self.Tab_envoye_widget_2 = Qt.QWidget()
        self.Tab_envoye_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_envoye_widget_2)
        self.Tab_envoye_grid_layout_2 = Qt.QGridLayout()
        self.Tab_envoye_layout_2.addLayout(self.Tab_envoye_grid_layout_2)
        self.Tab_envoye.addTab(self.Tab_envoye_widget_2, 'Autre_Button')
        self.Tab_envoye_widget_3 = Qt.QWidget()
        self.Tab_envoye_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_envoye_widget_3)
        self.Tab_envoye_grid_layout_3 = Qt.QGridLayout()
        self.Tab_envoye_layout_3.addLayout(self.Tab_envoye_grid_layout_3)
        self.Tab_envoye.addTab(self.Tab_envoye_widget_3, 'Tab 3')
        self.Tab_general_grid_layout_1.addWidget(self.Tab_envoye, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Tab_general_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_general_grid_layout_1.setColumnStretch(c, 1)
        self._on_off_recep_choices = {'Pressed': 1, 'Released': 0}

        _on_off_recep_toggle_switch = qtgui.GrToggleSwitch(self.set_on_off_recep, 'OFF-ON', self._on_off_recep_choices, False, "green", "red", 4, 50, 2, 1, self, 'value')
        self.on_off_recep = _on_off_recep_toggle_switch

        self.Tab_general_grid_layout_2.addWidget(_on_off_recep_toggle_switch, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Tab_general_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_general_grid_layout_2.setColumnStretch(c, 1)
        self._on_off_envoye_choices = {'Pressed': 1, 'Released': 0}

        _on_off_envoye_toggle_switch = qtgui.GrToggleSwitch(self.set_on_off_envoye, 'OFF-ON', self._on_off_envoye_choices, False, "green", "red", 4, 50, 2, 2, self, 'value')
        self.on_off_envoye = _on_off_envoye_toggle_switch

        self.Tab_general_grid_layout_1.addWidget(_on_off_envoye_toggle_switch, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Tab_general_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_general_grid_layout_1.setColumnStretch(c, 1)
        _envoye_bianire_push_button = Qt.QPushButton('Envoye')
        _envoye_bianire_push_button = Qt.QPushButton('Envoye')
        self._envoye_bianire_choices = {'Pressed': 1, 'Released': 0}
        _envoye_bianire_push_button.pressed.connect(lambda: self.set_envoye_bianire(self._envoye_bianire_choices['Pressed']))
        _envoye_bianire_push_button.released.connect(lambda: self.set_envoye_bianire(self._envoye_bianire_choices['Released']))
        self.Tab_envoye_layout_3.addWidget(_envoye_bianire_push_button)
        self._entre_Binaire_tool_bar = Qt.QToolBar(self)
        self._entre_Binaire_tool_bar.addWidget(Qt.QLabel("Entrez liste :" + ": "))
        self._entre_Binaire_line_edit = Qt.QLineEdit(str(self.entre_Binaire))
        self._entre_Binaire_tool_bar.addWidget(self._entre_Binaire_line_edit)
        self._entre_Binaire_line_edit.editingFinished.connect(
            lambda: self.set_entre_Binaire(eval(str(self._entre_Binaire_line_edit.text()))))
        self.Tab_envoye_layout_3.addWidget(self._entre_Binaire_tool_bar)
        self._code_D_tool_bar = Qt.QToolBar(self)

        if None:
            self._code_D_formatter = None
        else:
            self._code_D_formatter = lambda x: repr(x)

        self._code_D_tool_bar.addWidget(Qt.QLabel("Show_Code_D :"))
        self._code_D_label = Qt.QLabel(str(self._code_D_formatter(self.code_D)))
        self._code_D_tool_bar.addWidget(self._code_D_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._code_D_tool_bar, 5, 0, 1, 1)
        for r in range(5, 6):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)
        self._code_C_tool_bar = Qt.QToolBar(self)

        if None:
            self._code_C_formatter = None
        else:
            self._code_C_formatter = lambda x: repr(x)

        self._code_C_tool_bar.addWidget(Qt.QLabel("Show_Code_C :"))
        self._code_C_label = Qt.QLabel(str(self._code_C_formatter(self.code_C)))
        self._code_C_tool_bar.addWidget(self._code_C_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._code_C_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)
        self._code_B_tool_bar = Qt.QToolBar(self)

        if None:
            self._code_B_formatter = None
        else:
            self._code_B_formatter = lambda x: repr(x)

        self._code_B_tool_bar.addWidget(Qt.QLabel("Show_code_B :"))
        self._code_B_label = Qt.QLabel(str(self._code_B_formatter(self.code_B)))
        self._code_B_tool_bar.addWidget(self._code_B_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._code_B_tool_bar, 3, 0, 1, 1)
        for r in range(3, 4):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)
        self._code_A_et_B_et_C_et_D_tool_bar = Qt.QToolBar(self)

        if None:
            self._code_A_et_B_et_C_et_D_formatter = None
        else:
            self._code_A_et_B_et_C_et_D_formatter = lambda x: repr(x)

        self._code_A_et_B_et_C_et_D_tool_bar.addWidget(Qt.QLabel("Show_Code_A_et_B_et_C_et_D :"))
        self._code_A_et_B_et_C_et_D_label = Qt.QLabel(str(self._code_A_et_B_et_C_et_D_formatter(self.code_A_et_B_et_C_et_D)))
        self._code_A_et_B_et_C_et_D_tool_bar.addWidget(self._code_A_et_B_et_C_et_D_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._code_A_et_B_et_C_et_D_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)
        self._code_A_et_B_et_C_tool_bar = Qt.QToolBar(self)

        if None:
            self._code_A_et_B_et_C_formatter = None
        else:
            self._code_A_et_B_et_C_formatter = lambda x: repr(x)

        self._code_A_et_B_et_C_tool_bar.addWidget(Qt.QLabel("Show_code_A_et_B_et_C :"))
        self._code_A_et_B_et_C_label = Qt.QLabel(str(self._code_A_et_B_et_C_formatter(self.code_A_et_B_et_C)))
        self._code_A_et_B_et_C_tool_bar.addWidget(self._code_A_et_B_et_C_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._code_A_et_B_et_C_tool_bar, 7, 0, 1, 1)
        for r in range(7, 8):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)
        self._address_telec_tool_bar = Qt.QToolBar(self)

        if None:
            self._address_telec_formatter = None
        else:
            self._address_telec_formatter = lambda x: repr(x)

        self._address_telec_tool_bar.addWidget(Qt.QLabel("address_telec :"))
        self._address_telec_label = Qt.QLabel(str(self._address_telec_formatter(self.address_telec)))
        self._address_telec_tool_bar.addWidget(self._address_telec_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._address_telec_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)
        self.Tab_aff_recep_1 = Qt.QTabWidget()
        self.Tab_aff_recep_1_widget_0 = Qt.QWidget()
        self.Tab_aff_recep_1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_aff_recep_1_widget_0)
        self.Tab_aff_recep_1_grid_layout_0 = Qt.QGridLayout()
        self.Tab_aff_recep_1_layout_0.addLayout(self.Tab_aff_recep_1_grid_layout_0)
        self.Tab_aff_recep_1.addTab(self.Tab_aff_recep_1_widget_0, 'Affichage')
        self.Tab_recep_layout_0.addWidget(self.Tab_aff_recep_1)
        self.Tab_aff_envoye = Qt.QTabWidget()
        self.Tab_aff_envoye_widget_0 = Qt.QWidget()
        self.Tab_aff_envoye_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_aff_envoye_widget_0)
        self.Tab_aff_envoye_grid_layout_0 = Qt.QGridLayout()
        self.Tab_aff_envoye_layout_0.addLayout(self.Tab_aff_envoye_grid_layout_0)
        self.Tab_aff_envoye.addTab(self.Tab_aff_envoye_widget_0, 'Affichage')
        self.Tab_general_grid_layout_1.addWidget(self.Tab_aff_envoye, 2, 0, 1, 1)
        for r in range(2, 3):
            self.Tab_general_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_general_grid_layout_1.setColumnStretch(c, 1)
        _D_push_button = Qt.QPushButton('D')
        _D_push_button = Qt.QPushButton('D')
        self._D_choices = {'Pressed': 1, 'Released': 0}
        _D_push_button.pressed.connect(lambda: self.set_D(self._D_choices['Pressed']))
        _D_push_button.released.connect(lambda: self.set_D(self._D_choices['Released']))
        self.Tab_envoye_grid_layout_1.addWidget(_D_push_button, 3, 0, 1, 4)
        for r in range(3, 4):
            self.Tab_envoye_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.Tab_envoye_grid_layout_1.setColumnStretch(c, 1)
        self._Code_A_et_B_tool_bar = Qt.QToolBar(self)

        if None:
            self._Code_A_et_B_formatter = None
        else:
            self._Code_A_et_B_formatter = lambda x: repr(x)

        self._Code_A_et_B_tool_bar.addWidget(Qt.QLabel("Show_Code_A_et_B :"))
        self._Code_A_et_B_label = Qt.QLabel(str(self._Code_A_et_B_formatter(self.Code_A_et_B)))
        self._Code_A_et_B_tool_bar.addWidget(self._Code_A_et_B_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._Code_A_et_B_tool_bar, 6, 0, 1, 1)
        for r in range(6, 7):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)
        self._Code_A_tool_bar = Qt.QToolBar(self)

        if None:
            self._Code_A_formatter = None
        else:
            self._Code_A_formatter = lambda x: repr(x)

        self._Code_A_tool_bar.addWidget(Qt.QLabel("Show_Code_A :"))
        self._Code_A_label = Qt.QLabel(str(self._Code_A_formatter(self.Code_A)))
        self._Code_A_tool_bar.addWidget(self._Code_A_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._Code_A_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)
        _C_push_button = Qt.QPushButton('C')
        _C_push_button = Qt.QPushButton('C')
        self._C_choices = {'Pressed': 1, 'Released': 0}
        _C_push_button.pressed.connect(lambda: self.set_C(self._C_choices['Pressed']))
        _C_push_button.released.connect(lambda: self.set_C(self._C_choices['Released']))
        self.Tab_envoye_grid_layout_1.addWidget(_C_push_button, 2, 0, 1, 4)
        for r in range(2, 3):
            self.Tab_envoye_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.Tab_envoye_grid_layout_1.setColumnStretch(c, 1)
        _B_push_button = Qt.QPushButton('B')
        _B_push_button = Qt.QPushButton('B')
        self._B_choices = {'Pressed': 1, 'Released': 0}
        _B_push_button.pressed.connect(lambda: self.set_B(self._B_choices['Pressed']))
        _B_push_button.released.connect(lambda: self.set_B(self._B_choices['Released']))
        self.Tab_envoye_grid_layout_1.addWidget(_B_push_button, 1, 0, 1, 4)
        for r in range(1, 2):
            self.Tab_envoye_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.Tab_envoye_grid_layout_1.setColumnStretch(c, 1)
        _A_et_B_et_C_et_D_push_button = Qt.QPushButton('A_et_B_et_C_et_D')
        _A_et_B_et_C_et_D_push_button = Qt.QPushButton('A_et_B_et_C_et_D')
        self._A_et_B_et_C_et_D_choices = {'Pressed': 1, 'Released': 0}
        _A_et_B_et_C_et_D_push_button.pressed.connect(lambda: self.set_A_et_B_et_C_et_D(self._A_et_B_et_C_et_D_choices['Pressed']))
        _A_et_B_et_C_et_D_push_button.released.connect(lambda: self.set_A_et_B_et_C_et_D(self._A_et_B_et_C_et_D_choices['Released']))
        self.Tab_envoye_grid_layout_2.addWidget(_A_et_B_et_C_et_D_push_button, 2, 0, 1, 4)
        for r in range(2, 3):
            self.Tab_envoye_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.Tab_envoye_grid_layout_2.setColumnStretch(c, 1)
        _A_et_B_et_C_push_button = Qt.QPushButton('A_et_B_et_C')
        _A_et_B_et_C_push_button = Qt.QPushButton('A_et_B_et_C')
        self._A_et_B_et_C_choices = {'Pressed': 1, 'Released': 0}
        _A_et_B_et_C_push_button.pressed.connect(lambda: self.set_A_et_B_et_C(self._A_et_B_et_C_choices['Pressed']))
        _A_et_B_et_C_push_button.released.connect(lambda: self.set_A_et_B_et_C(self._A_et_B_et_C_choices['Released']))
        self.Tab_envoye_grid_layout_2.addWidget(_A_et_B_et_C_push_button, 1, 0, 1, 4)
        for r in range(1, 2):
            self.Tab_envoye_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.Tab_envoye_grid_layout_2.setColumnStretch(c, 1)
        _A_et_B_push_button = Qt.QPushButton('A_et_B')
        _A_et_B_push_button = Qt.QPushButton('A_et_B')
        self._A_et_B_choices = {'Pressed': 1, 'Released': 0}
        _A_et_B_push_button.pressed.connect(lambda: self.set_A_et_B(self._A_et_B_choices['Pressed']))
        _A_et_B_push_button.released.connect(lambda: self.set_A_et_B(self._A_et_B_choices['Released']))
        self.Tab_envoye_grid_layout_2.addWidget(_A_et_B_push_button, 0, 0, 1, 4)
        for r in range(0, 1):
            self.Tab_envoye_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.Tab_envoye_grid_layout_2.setColumnStretch(c, 1)
        _A_push_button = Qt.QPushButton('A')
        _A_push_button = Qt.QPushButton('A')
        self._A_choices = {'Pressed': 1, 'Released': 0}
        _A_push_button.pressed.connect(lambda: self.set_A(self._A_choices['Pressed']))
        _A_push_button.released.connect(lambda: self.set_A(self._A_choices['Released']))
        self.Tab_envoye_grid_layout_1.addWidget(_A_push_button, 0, 0, 1, 4)
        for r in range(0, 1):
            self.Tab_envoye_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.Tab_envoye_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_sink_x_0_1_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_recep, #bw
            "Singal reçu", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1_0.enable_rf_freq(False)

        self.Tab_recep_layout_0.addWidget(self._qtgui_sink_x_0_1_0_win)
        self.qtgui_sink_x_0_1 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_envoye, #bw
            "Singal envoyer", #name
            True, #plotfreq
            False, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1.enable_rf_freq(False)

        self.Tab_aff_envoye_grid_layout_0.addWidget(self._qtgui_sink_x_0_1_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.Tab_aff_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.Tab_aff_envoye_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_sink_x_0_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_recep, #bw
            "Binaire", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0.enable_rf_freq(False)

        self.Tab_recep_layout_0.addWidget(self._qtgui_sink_x_0_0_0_win)
        self.qtgui_sink_x_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_envoye, #bw
            "Binaire", #name
            True, #plotfreq
            False, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.Tab_aff_envoye_grid_layout_0.addWidget(self._qtgui_sink_x_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Tab_aff_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_aff_envoye_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_recep, #bw
            "Apres demodulation", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.Tab_recep_layout_0.addWidget(self._qtgui_sink_x_0_win)
        self.qtgui_graphicitem_0_0_1_0 = self._qtgui_graphicitem_0_0_1_0_win = qtgui.GrGraphicItem('C:\\Users\\basti\\OneDrive\\Bureau\\IUT\\Semestre 3\\SAE 31 - Etude et mise en oeuvre d’un système de transmission\\Capture d’écran 2024-10-25 152410.png',False,True,750,750)
        self._qtgui_graphicitem_0_0_1_0_win = self._qtgui_graphicitem_0_0_1_0_win
        self.Tab_general_grid_layout_1.addWidget(self._qtgui_graphicitem_0_0_1_0_win, 3, 0, 4, 1)
        for r in range(3, 7):
            self.Tab_general_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_general_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_graphicitem_0_0_1 = self._qtgui_graphicitem_0_0_1_win = qtgui.GrGraphicItem('C:\\Users\\basti\\OneDrive\\Bureau\\IUT\\Semestre 3\\SAE 31 - Etude et mise en oeuvre d’un système de transmission\\Capture d’écran 2024-10-25 152410.png',False,True,750,750)
        self._qtgui_graphicitem_0_0_1_win = self._qtgui_graphicitem_0_0_1_win
        self.Tab_general_grid_layout_0.addWidget(self._qtgui_graphicitem_0_0_1_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.Tab_general_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.Tab_general_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_graphicitem_0_0_0 = self._qtgui_graphicitem_0_0_0_win = qtgui.GrGraphicItem('C:\\Users\\basti\\OneDrive\\Bureau\\IUT\\Semestre 3\\SAE 31 - Etude et mise en oeuvre d’un système de transmission\\Capture d’écran 2024-10-25 152410.png',False,True,750,750)
        self._qtgui_graphicitem_0_0_0_win = self._qtgui_graphicitem_0_0_0_win
        self.Tab_general_grid_layout_0.addWidget(self._qtgui_graphicitem_0_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Tab_general_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_general_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_graphicitem_0_0 = self._qtgui_graphicitem_0_0_win = qtgui.GrGraphicItem('C:\\Users\\basti\\OneDrive\\Bureau\\IUT\\Semestre 3\\SAE 31 - Etude et mise en oeuvre d’un système de transmission\\Capture d’écran 2024-10-25 152410.png',False,True,(-1),(-1))
        self._qtgui_graphicitem_0_0_win = self._qtgui_graphicitem_0_0_win
        self.Tab_general_grid_layout_0.addWidget(self._qtgui_graphicitem_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Tab_general_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_general_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_graphicitem_0 = self._qtgui_graphicitem_0_win = qtgui.GrGraphicItem('C:\\Users\\basti\\OneDrive\\Bureau\\IUT\\Semestre 3\\SAE 31 - Etude et mise en oeuvre d’un système de transmission\\Capture d’écran 2024-10-25 151529.png',False,True,640,640)
        self._qtgui_graphicitem_0_win = self._qtgui_graphicitem_0_win
        self.Tab_general_grid_layout_0.addWidget(self._qtgui_graphicitem_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.Tab_general_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.Tab_general_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_recep, #bw
            "Apres filtre", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.Tab_aff_recep_1_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.Tab_aff_recep_1_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.Tab_aff_recep_1_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_recep, #bw
            "Avant Filtre", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

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

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.Tab_aff_recep_1_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Tab_aff_recep_1_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_aff_recep_1_grid_layout_0.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                100000,
                500,
                100,
                window.WIN_HAMMING,
                6.76))
        self.iio_pluto_source_0_0 = iio.fmcomms2_source_fc32('ip:192.168.2.1' if 'ip:192.168.2.1' else iio.get_pluto_uri(), [True, True], 32768)
        self.iio_pluto_source_0_0.set_len_tag_key('packet_len')
        self.iio_pluto_source_0_0.set_frequency(Frequency)
        self.iio_pluto_source_0_0.set_samplerate(2000000)
        self.iio_pluto_source_0_0.set_gain_mode(0, 'slow_attack')
        self.iio_pluto_source_0_0.set_gain(0, 64)
        self.iio_pluto_source_0_0.set_quadrature(True)
        self.iio_pluto_source_0_0.set_rfdc(True)
        self.iio_pluto_source_0_0.set_bbdc(True)
        self.iio_pluto_source_0_0.set_filter_params('Auto', '', 0, 0)
        self.iio_pluto_sink_0 = iio.fmcomms2_sink_fc32('ip:192.168.2.1' if 'ip:192.168.2.1' else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_0.set_len_tag_key('')
        self.iio_pluto_sink_0.set_bandwidth(20000000)
        self.iio_pluto_sink_0.set_frequency(Frequency)
        self.iio_pluto_sink_0.set_samplerate(samp_rate_envoye)
        self.iio_pluto_sink_0.set_attenuation(0, 10.0)
        self.iio_pluto_sink_0.set_filter_params('Auto', '', 0, 0)
        self.epy_block_1_0_2_0 = epy_block_1_0_2_0.concat_source_block(var1=Prémbule, var2=address_telec, var3=Code_A_et_B)
        self.epy_block_1_0_2 = epy_block_1_0_2.concat_source_block(var1=Prémbule, var2=address_telec, var3=Code_A)
        self.epy_block_1_0_1_0 = epy_block_1_0_1_0.concat_source_block(var1=Prémbule, var2=address_telec, var3=code_A_et_B_et_C_et_D)
        self.epy_block_1_0_1 = epy_block_1_0_1.concat_source_block(var1=Prémbule, var2=address_telec, var3=code_C)
        self.epy_block_1_0_0_0 = epy_block_1_0_0_0.concat_source_block(var1=Prémbule, var2=address_telec, var3=code_A_et_B_et_C)
        self.epy_block_1_0_0 = epy_block_1_0_0.concat_source_block(var1=Prémbule, var2=address_telec, var3=code_B)
        self.epy_block_1_0 = epy_block_1_0.concat_source_block(var1=Prémbule, var2=address_telec, var3=code_D)
        self._copyrightMB_tool_bar = Qt.QToolBar(self)

        if None:
            self._copyrightMB_formatter = None
        else:
            self._copyrightMB_formatter = lambda x: str(x)

        self._copyrightMB_tool_bar.addWidget(Qt.QLabel("copyright :"))
        self._copyrightMB_label = Qt.QLabel(str(self._copyrightMB_formatter(self.copyrightMB)))
        self._copyrightMB_tool_bar.addWidget(self._copyrightMB_label)
        self.top_grid_layout.addWidget(self._copyrightMB_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_vector_source_x_0 = blocks.vector_source_f(entre_Binaire, True, 1, [])
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0.01, 0.15, 0)
        self.blocks_repeat_0_3 = blocks.repeat(gr.sizeof_float*1, 350)
        self.blocks_repeat_0_2_0 = blocks.repeat(gr.sizeof_float*1, 350)
        self.blocks_repeat_0_2 = blocks.repeat(gr.sizeof_float*1, 350)
        self.blocks_repeat_0_1_0 = blocks.repeat(gr.sizeof_float*1, 350)
        self.blocks_repeat_0_1 = blocks.repeat(gr.sizeof_float*1, 350)
        self.blocks_repeat_0_0_0 = blocks.repeat(gr.sizeof_float*1, 350)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_float*1, 350)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, 350)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1_5 = blocks.multiply_const_ff(A_et_B)
        self.blocks_multiply_const_vxx_1_4_3 = blocks.multiply_const_ff(on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_2_0 = blocks.multiply_const_ff(on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_2 = blocks.multiply_const_ff(on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_1_0 = blocks.multiply_const_ff(on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_1 = blocks.multiply_const_ff(on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_0_0 = blocks.multiply_const_ff(on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_0 = blocks.multiply_const_ff(on_off_envoye)
        self.blocks_multiply_const_vxx_1_4 = blocks.multiply_const_ff(on_off_envoye)
        self.blocks_multiply_const_vxx_1_3 = blocks.multiply_const_cc(on_off_recep)
        self.blocks_multiply_const_vxx_1_2_0 = blocks.multiply_const_ff(A_et_B_et_C_et_D)
        self.blocks_multiply_const_vxx_1_2 = blocks.multiply_const_ff(C)
        self.blocks_multiply_const_vxx_1_1_0 = blocks.multiply_const_ff(A_et_B_et_C)
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_ff(B)
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_ff(envoye_bianire)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_ff(D)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(A)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, 'test.raw', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0 = analog.sig_source_f(1000000, analog.GR_COS_WAVE, Frequency, 1, 0, 0)
        self._Prémbule_tool_bar = Qt.QToolBar(self)

        if None:
            self._Prémbule_formatter = None
        else:
            self._Prémbule_formatter = lambda x: repr(x)

        self._Prémbule_tool_bar.addWidget(Qt.QLabel("Prémbule :"))
        self._Prémbule_label = Qt.QLabel(str(self._Prémbule_formatter(self.Prémbule)))
        self._Prémbule_tool_bar.addWidget(self._Prémbule_label)
        self.Tab_envoye_grid_layout_0.addWidget(self._Prémbule_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Tab_envoye_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Tab_envoye_grid_layout_0.setColumnStretch(c, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_sink_x_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_1_0, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.blocks_multiply_const_vxx_1_2, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_2_0, 0), (self.blocks_add_xx_0, 6))
        self.connect((self.blocks_multiply_const_vxx_1_3, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_3, 0), (self.qtgui_sink_x_0_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_4, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_4_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_4_0_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_4_1, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_4_1_0, 0), (self.blocks_multiply_const_vxx_1_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_4_2, 0), (self.blocks_multiply_const_vxx_1_2, 0))
        self.connect((self.blocks_multiply_const_vxx_1_4_2_0, 0), (self.blocks_multiply_const_vxx_1_2_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_4_3, 0), (self.blocks_multiply_const_vxx_1_5, 0))
        self.connect((self.blocks_multiply_const_vxx_1_5, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_const_vxx_1_4, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_multiply_const_vxx_1_4_1, 0))
        self.connect((self.blocks_repeat_0_0_0, 0), (self.blocks_multiply_const_vxx_1_4_1_0, 0))
        self.connect((self.blocks_repeat_0_1, 0), (self.blocks_multiply_const_vxx_1_4_2, 0))
        self.connect((self.blocks_repeat_0_1_0, 0), (self.blocks_multiply_const_vxx_1_4_2_0, 0))
        self.connect((self.blocks_repeat_0_2, 0), (self.blocks_multiply_const_vxx_1_4_0, 0))
        self.connect((self.blocks_repeat_0_2_0, 0), (self.blocks_multiply_const_vxx_1_4_0_0, 0))
        self.connect((self.blocks_repeat_0_3, 0), (self.blocks_multiply_const_vxx_1_4_3, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.qtgui_sink_x_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0_2_0, 0))
        self.connect((self.epy_block_1_0, 0), (self.blocks_repeat_0_2, 0))
        self.connect((self.epy_block_1_0_0, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.epy_block_1_0_0_0, 0), (self.blocks_repeat_0_0_0, 0))
        self.connect((self.epy_block_1_0_1, 0), (self.blocks_repeat_0_1, 0))
        self.connect((self.epy_block_1_0_1_0, 0), (self.blocks_repeat_0_1_0, 0))
        self.connect((self.epy_block_1_0_2, 0), (self.blocks_repeat_0, 0))
        self.connect((self.epy_block_1_0_2_0, 0), (self.blocks_repeat_0_3, 0))
        self.connect((self.iio_pluto_source_0_0, 0), (self.blocks_multiply_const_vxx_1_3, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Telecommande")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate_recep(self):
        return self.samp_rate_recep

    def set_samp_rate_recep(self, samp_rate_recep):
        self.samp_rate_recep = samp_rate_recep
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate_recep)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate_recep)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate_recep)
        self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate_recep)
        self.qtgui_sink_x_0_1_0.set_frequency_range(0, self.samp_rate_recep)

    def get_samp_rate_envoye(self):
        return self.samp_rate_envoye

    def set_samp_rate_envoye(self, samp_rate_envoye):
        self.samp_rate_envoye = samp_rate_envoye
        self.iio_pluto_sink_0.set_samplerate(self.samp_rate_envoye)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate_envoye)
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate_envoye)

    def get_on_off_recep(self):
        return self.on_off_recep

    def set_on_off_recep(self, on_off_recep):
        self.on_off_recep = on_off_recep
        self.blocks_multiply_const_vxx_1_3.set_k(self.on_off_recep)

    def get_on_off_envoye(self):
        return self.on_off_envoye

    def set_on_off_envoye(self, on_off_envoye):
        self.on_off_envoye = on_off_envoye
        self.blocks_multiply_const_vxx_1_4.set_k(self.on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_0.set_k(self.on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_0_0.set_k(self.on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_1.set_k(self.on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_1_0.set_k(self.on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_2.set_k(self.on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_2_0.set_k(self.on_off_envoye)
        self.blocks_multiply_const_vxx_1_4_3.set_k(self.on_off_envoye)

    def get_envoye_bianire(self):
        return self.envoye_bianire

    def set_envoye_bianire(self, envoye_bianire):
        self.envoye_bianire = envoye_bianire
        self.blocks_multiply_const_vxx_1_0_0.set_k(self.envoye_bianire)

    def get_entre_Binaire(self):
        return self.entre_Binaire

    def set_entre_Binaire(self, entre_Binaire):
        self.entre_Binaire = entre_Binaire
        Qt.QMetaObject.invokeMethod(self._entre_Binaire_line_edit, "setText", Qt.Q_ARG("QString", repr(self.entre_Binaire)))
        self.blocks_vector_source_x_0.set_data(self.entre_Binaire, [])

    def get_copyrightMB(self):
        return self.copyrightMB

    def set_copyrightMB(self, copyrightMB):
        self.copyrightMB = copyrightMB
        Qt.QMetaObject.invokeMethod(self._copyrightMB_label, "setText", Qt.Q_ARG("QString", str(self._copyrightMB_formatter(self.copyrightMB))))

    def get_code_D(self):
        return self.code_D

    def set_code_D(self, code_D):
        self.code_D = code_D
        Qt.QMetaObject.invokeMethod(self._code_D_label, "setText", Qt.Q_ARG("QString", str(self._code_D_formatter(self.code_D))))
        self.epy_block_1_0.var3 = self.code_D

    def get_code_C(self):
        return self.code_C

    def set_code_C(self, code_C):
        self.code_C = code_C
        Qt.QMetaObject.invokeMethod(self._code_C_label, "setText", Qt.Q_ARG("QString", str(self._code_C_formatter(self.code_C))))
        self.epy_block_1_0_1.var3 = self.code_C

    def get_code_B(self):
        return self.code_B

    def set_code_B(self, code_B):
        self.code_B = code_B
        Qt.QMetaObject.invokeMethod(self._code_B_label, "setText", Qt.Q_ARG("QString", str(self._code_B_formatter(self.code_B))))
        self.epy_block_1_0_0.var3 = self.code_B

    def get_code_A_et_B_et_C_et_D(self):
        return self.code_A_et_B_et_C_et_D

    def set_code_A_et_B_et_C_et_D(self, code_A_et_B_et_C_et_D):
        self.code_A_et_B_et_C_et_D = code_A_et_B_et_C_et_D
        Qt.QMetaObject.invokeMethod(self._code_A_et_B_et_C_et_D_label, "setText", Qt.Q_ARG("QString", str(self._code_A_et_B_et_C_et_D_formatter(self.code_A_et_B_et_C_et_D))))
        self.epy_block_1_0_1_0.var3 = self.code_A_et_B_et_C_et_D

    def get_code_A_et_B_et_C(self):
        return self.code_A_et_B_et_C

    def set_code_A_et_B_et_C(self, code_A_et_B_et_C):
        self.code_A_et_B_et_C = code_A_et_B_et_C
        Qt.QMetaObject.invokeMethod(self._code_A_et_B_et_C_label, "setText", Qt.Q_ARG("QString", str(self._code_A_et_B_et_C_formatter(self.code_A_et_B_et_C))))
        self.epy_block_1_0_0_0.var3 = self.code_A_et_B_et_C

    def get_address_telec(self):
        return self.address_telec

    def set_address_telec(self, address_telec):
        self.address_telec = address_telec
        Qt.QMetaObject.invokeMethod(self._address_telec_label, "setText", Qt.Q_ARG("QString", str(self._address_telec_formatter(self.address_telec))))
        self.epy_block_1_0.var2 = self.address_telec
        self.epy_block_1_0_0.var2 = self.address_telec
        self.epy_block_1_0_0_0.var2 = self.address_telec
        self.epy_block_1_0_1.var2 = self.address_telec
        self.epy_block_1_0_1_0.var2 = self.address_telec
        self.epy_block_1_0_2.var2 = self.address_telec
        self.epy_block_1_0_2_0.var2 = self.address_telec

    def get_Prémbule(self):
        return self.Prémbule

    def set_Prémbule(self, Prémbule):
        self.Prémbule = Prémbule

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency
        self.analog_sig_source_x_0.set_frequency(self.Frequency)
        self.iio_pluto_sink_0.set_frequency(self.Frequency)
        self.iio_pluto_source_0_0.set_frequency(self.Frequency)

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.blocks_multiply_const_vxx_1_0.set_k(self.D)

    def get_Code_A_et_B(self):
        return self.Code_A_et_B

    def set_Code_A_et_B(self, Code_A_et_B):
        self.Code_A_et_B = Code_A_et_B
        Qt.QMetaObject.invokeMethod(self._Code_A_et_B_label, "setText", Qt.Q_ARG("QString", str(self._Code_A_et_B_formatter(self.Code_A_et_B))))
        self.epy_block_1_0_2_0.var3 = self.Code_A_et_B

    def get_Code_A(self):
        return self.Code_A

    def set_Code_A(self, Code_A):
        self.Code_A = Code_A
        Qt.QMetaObject.invokeMethod(self._Code_A_label, "setText", Qt.Q_ARG("QString", str(self._Code_A_formatter(self.Code_A))))
        self.epy_block_1_0_2.var3 = self.Code_A

    def get_C(self):
        return self.C

    def set_C(self, C):
        self.C = C
        self.blocks_multiply_const_vxx_1_2.set_k(self.C)

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.blocks_multiply_const_vxx_1_1.set_k(self.B)

    def get_A_et_B_et_C_et_D(self):
        return self.A_et_B_et_C_et_D

    def set_A_et_B_et_C_et_D(self, A_et_B_et_C_et_D):
        self.A_et_B_et_C_et_D = A_et_B_et_C_et_D
        self.blocks_multiply_const_vxx_1_2_0.set_k(self.A_et_B_et_C_et_D)

    def get_A_et_B_et_C(self):
        return self.A_et_B_et_C

    def set_A_et_B_et_C(self, A_et_B_et_C):
        self.A_et_B_et_C = A_et_B_et_C
        self.blocks_multiply_const_vxx_1_1_0.set_k(self.A_et_B_et_C)

    def get_A_et_B(self):
        return self.A_et_B

    def set_A_et_B(self, A_et_B):
        self.A_et_B = A_et_B
        self.blocks_multiply_const_vxx_1_5.set_k(self.A_et_B)

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.blocks_multiply_const_vxx_1.set_k(self.A)




def main(top_block_cls=Telecommande, options=None):

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
