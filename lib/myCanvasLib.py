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

import numpy as np

import PySide
from PySide import QtGui  # QtGui.QMainWindow, QtGui.QPushButton, QtGui.QApplication

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# plt.ion()

class MyMplCanvas(FigureCanvas):
    """
    Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.).
    But I connected this to graphicsView in the ui
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure()#figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')        
        
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        plt.show()

        # self.ani = animation.FuncAnimation(fig, updateImage, data_gen, interval=100)

    def plotImage(self, image):
        # self.axes.cla()
        self.img = self.axes.imshow(image, interpolation='nearest', cmap='gray')#, animated=True)
        self.draw()
    
    # def updateImage(self, image):
    #     self.img.set_data(image)
    #     self.draw()
    #     # return self.img
