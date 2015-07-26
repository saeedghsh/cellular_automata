# "
# Copyright (C) 2015 Saeed Gholami Shahbandi. All rights reserved.

# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this program. If not, see
# <http://www.gnu.org/licenses/>
# "

import sys, os, platform, time
import threading

import numpy as np
import PySide
from PySide import QtCore, QtGui

sys.path.append('../gui/')
import GOL # GOL.Ui_MainWindow
import myCanvasLib as MCL
import GameOfLifeLib as GOLib
reload(MCL)
reload(GOLib)



import matplotlib.pyplot as plt
import matplotlib.animation as animation


class MainWindow(QtGui.QMainWindow, GOL.Ui_MainWindow):
    def __init__(self, parent=None):
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
        self.ui.changeSizeButton.clicked.connect(self.initiateCA)
        self.ui.initAliveButton.clicked.connect(self.initiateCA)
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)

        self.initiateCA()
        
        # self.thread = threading.Thread(name='playIteration', target=self.playIteration)
        # self.thread.setDaemon(True)
        # self.thread.start()
       
            
    def initiateCA(self):
        gridSize = int(self.ui.sizeValue.toPlainText())
        rule = self.ui.ruleScroll.currentText()
        cellType =  self.ui.cellTypeScroll.currentText()
        self.cellAut = GOLib.CellularAutomata([gridSize,gridSize], rule=rule, cellType=cellType)
        self.cellAut.giveBirth(percent=float(self.ui.initAlive.toPlainText()))
        self.myCanvas.plotImage(self.cellAut.grid)
       

    def start(self):
        print 'hello'
        self.play = True
        self.ani = animation.FuncAnimation(self.myCanvas.figure,
                                           self.myCanvas.updateImage,
                                           self.iterate,
                                           interval= 1/self.ui.speedSlider.sliderPosition())


    def stop(self):
        print 'goodbye'
        self.play = False


    def iterate(self):
        while self.play: yield self.cellAut.iterate()


    ###################################################################
    def mouseClick(self, event):
        # self.temp.append([event.xdata, event.ydata])
        pass

    def about(self):
        QtGui.QMessageBox.about(self, "About Game of Life",
                                """<b>Version</b> %s
                                <p>Copyright &copy; 2015 Saeed Gholami Shahbandi.
                                All rights reserved in accordance with
                                BSD 3-clause - NO WARRANTIES!
                                <p>This GUI is a simple implementation of Game of Life.
                                <p>Python %s - PySide version %s - Qt version %s on %s""" % (__version__,
                                                                                             platform.python_version(), PySide.__version__, QtCore.__version__,
                                                                                             platform.system()))
