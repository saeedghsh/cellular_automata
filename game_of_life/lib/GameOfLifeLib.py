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
from __future__ import print_function
import numpy as np

################################################################################
################################################################################
################################################################################
class CellularAutomata:
    ''''''
    def __init__(self, gridSize, rule='conway', neighborhoodRange=1, cellType='square'):
        ''''''
        ## all internal variables
        self.size = gridSize #(r,c)
        self.cellType = cellType
        self.nRange = neighborhoodRange

        if rule == 'conway':
            self.rule = self.conway
        else:
            raise( NameError('No other rule other than Conway is defined yet...') )

        #generateGrid
        if self.cellType == 'square':
            self.grid = np.zeros(self.size)
        elif self.cellType == 'hexagon':
            raise( NameError('hexagon cell type is not supported yet...') )
        elif self.cellType == 'triangle':
            raise( NameError('triangle cell type is not supported yet...') )

    ########################################
    def giveBirth (self, percent=0.2, mode='rand'):
        ''''''
        if mode == 'rand':
            for i in np.arange(percent*self.size[0]*self.size[1]):
                c = np.random.random_integers(self.size[0]-1)
                r = np.random.random_integers(self.size[1]-1)
                self.grid[c][r] = 1
        elif mode == 'template':
            pass

    ########################################        
    def calcNeighborSum(self):
        ''''''
        if self.cellType == 'square':
            '''
            instead of adding values of the neighbors one by one,
            the image is shifted and sum up shifted images into "neighborSum".
            the result will be the summation of neighbors, plus the value of cell itself.
            that's why the "neighborSum" is initiated with negative of self.grid
            '''
            
            x = self.grid
            nr = self.nRange
            
            # creating a bigger grid with padding on margins
            # and putting the original grid at the center of the new grid
            # this grid is used for shifting
            y = np.zeros([x.shape[0]+2*nr,x.shape[1]+2*nr])
            y[nr:-nr,nr:-nr] = x
            
            # the same as previous, but for storing the result of summation
            neighborSum = np.zeros([x.shape[0]+2*nr,x.shape[1]+2*nr])
            neighborSum[nr:-nr,nr:-nr] = -x

            # shifting the image and accumulate it in the "neighborSum"
            for r in np.arange(-nr,nr+1):
                y_ = np.roll(y, r, axis=0)
                for c in np.arange(-nr,nr+1):
                    neighborSum += np.roll(y_, c, axis=1)

            # removing the margins 
            self.neighborSum = neighborSum[nr:-nr,nr:-nr]

        elif self.cellType == 'hexagon':
            raise( NameError('hexagon cell type is not supported yet...') )
        elif self.cellType == 'triangle':
            raise( NameError('triangle cell type is not supported yet...') )

    ########################################
    def conway(self, come2life=None, stayAlive=None):
        '''
        '''
        if come2life is None: come2life=[3]
        if stayAlive is None: stayAlive=[2,3]
        assert type(come2life) == type(stayAlive) == list

        ##### come2life
        # (condition1: be dead, condition1: have alive neighbours equal to come2life)
        mask1 = self.grid==0
        mask2 = np.any(np.array([self.neighborSum == n for n in come2life]), axis=0)
        come2life_mask = np.logical_and(mask1,mask2)
        
        ##### stayAlive
        # (condition1: be alive, condition1: have alive neighbours equal to stayAlive)
        mask1 = self.grid==1
        mask2 = np.any(np.array([self.neighborSum == n for n in stayAlive]), axis=0)
        stayAlive_mask = np.logical_and(mask1,mask2)

        return np.where( np.logical_or(come2life_mask, stayAlive_mask), 1., 0.)

    ########################################
    def iterate(self):
        '''
        '''
        self.calcNeighborSum()
        self.grid = self.rule()
        # return self.grid




################################################################################
########################################################################### Demo
################################################################################
if __name__ == '__main__':
    '''
    '''
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    myAut = CellularAutomata(gridSize=[200,200])
    myAut.giveBirth()

    ##### crude animation
    if 0: 
        fig, axes = plt.subplots(1,1, figsize=(10,10))
        p = axes.imshow(myAut.grid, cmap='gray', interpolation='nearest', origin='lower')
        
        for i in range(100):
            print("step", i)
            myAut.iterate()
            p.set_data(myAut.grid)
            plt.pause(.1**10)

    ##### more complex animation
    if 0:
        fig, axes = plt.subplots(1,1, figsize=(10,10))
        p = axes.imshow(myAut.grid, cmap='gray', interpolation='nearest', origin='lower')

        def update(data):
            p.set_data(data)
            return p,

        def data_gen():
            global myAut
            myAut.iterate()
            yield myAut.grid

        ani = matplotlib.animation.FuncAnimation(fig, update, data_gen, interval=1000)
        plt.show()
        
    ##### animation with pause
    if 1:
    
        pause = False

        def data_gen():
            if not pause:
                myAut.iterate()
                yield myAut.grid

        def onClick(event):
            global pause
            pause ^= True

            if pause:
                global ani
                ani._stop()
            else:
                ani = animation.FuncAnimation(fig, update, data_gen, blit=True, interval=10)


        def update(data):
            p.set_data(data)
            return p,

        fig, axes = plt.subplots(1,1, figsize=(10,10))
        fig.canvas.mpl_connect('button_press_event', onClick)
        
        p = axes.imshow(myAut.grid, cmap='gray', interpolation='nearest', origin='lower')
        
        ani = animation.FuncAnimation(fig, update, data_gen, blit=True, interval=10)
        plt.show()
