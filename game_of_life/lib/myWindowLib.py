'''
Copyright (C) 2015 Saeed Gholami Shahbandi. All rights reserved.

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public License
as published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this program. If not, see
<http://www.gnu.org/licenses/>
'''

import sys, os, platform, time
from functools import partial

import numpy as np
import PySide
from PySide import QtCore, QtGui

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import GOL
import myCanvasLib as MCL
import GameOfLifeLib as GOLib


################################################################################
################################################################################
################################################################################
class MainWindow(QtGui.QMainWindow, GOL.Ui_MainWindow):
    '''
    '''
    def __init__(self, parent=None):
        ''''''
        super(MainWindow, self).__init__(parent)
        self.ui = GOL.Ui_MainWindow()
        self.ui.setupUi(self)

        ## Matplotlib Setting
        self.main_widget = self.ui.graphicsView #QtGui.QWidget(self)
        self.layout = QtGui.QVBoxLayout(self.main_widget)
        self.myCanvas = MCL.MyMplCanvas(self.main_widget)#, width=5, height=4, dpi=100)
        self.layout.addWidget(self.myCanvas)
        self.main_widget.setFocus()
        self.myCanvas.mpl_connect('button_press_event', self.mouseClick)
        
        ## Push buttons
        self.ui.changeSizeButton.clicked.connect(self.initiate)
        self.ui.initAliveButton.clicked.connect(self.initiate)
        self.ui.resetButton.clicked.connect(self.initiate)
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)

        self.animation = None        
        self.initiate()
        
    ########################################
    def initiate(self):
        ''''''
        if type(self.animation) == animation.FuncAnimation:
            # if self.animation already exists, it should be stoped
            try:
                # in case animation is already stoped and cannot remove call_back
                self.animation._stop()
            except:
                pass

        self.play = False

        gridSize = int(self.ui.sizeValue.toPlainText())
        rule = self.ui.ruleScroll.currentText()
        cellType =  self.ui.cellTypeScroll.currentText()

        self.cellAut = GOLib.CellularAutomata([gridSize,gridSize], rule=rule, cellType=cellType)
        self.cellAut.giveBirth(percent=float(self.ui.initAlive.toPlainText()))
        self.myCanvas.plotImage(self.cellAut.grid)

    ########################################
    def start(self):
        ''''''
        self.play = True
        interval = self.ui.speedSlider.sliderPosition()
        self.animation = animation.FuncAnimation(self.myCanvas.fig,
                                                 self.update_plot,
                                                 self.generate_plot,
                                                 blit=True,
                                                 interval=interval)

    ########################################
    def stop(self):
        ''''''
        self.play = False

        if type(self.animation) == animation.FuncAnimation:
            # only if self.animation already exists
            try:
                # in case animation is already stoped and cannot remove call_back
                self.animation._stop()
            except:
                pass

    ########################################
    def generate_plot(self):
        ''''''
        if self.play:
            self.cellAut.iterate()
            yield self.cellAut.grid

    ########################################
    def update_plot(self, data):
        ''''''
        self.myCanvas.img.set_data(data)
        return self.myCanvas.img,

    ###################################################################
    def mouseClick(self, event):
        ''''''
        # print([event.xdata, event.ydata])
        # self.play ^= True
        pass

    ########################################
    def about(self):
        ''''''
        msg = 'Version</b> {:s}, Python {:s}, PySide version {:s}, Qt version {:s} on {:s}'
        QtGui.QMessageBox.about(self,
                                'About Game of Life',
                                msg.format(__version__,
                                           platform.python_version(),
                                           PySide.__version__,
                                           QtCore.__version__, platform.system()))
        
