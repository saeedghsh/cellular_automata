import numpy as np

########################################
class CellularAutomata:
    def __init__(self, gridSize, rule='conway', neighborhoodRange=1, cellType='square'):
        ## all internal variables
        self.size = gridSize #(r,c)
        self.cellType = cellType
        self.nRange = neighborhoodRange

        if rule == 'conway':
            self.rule = self.conway
        elif rule == 'xxx':
            pass

        #generateGrid
        if self.cellType == 'square':
            self.grid = np.zeros(self.size)
        elif self.cellType == 'hexagon': pass #TODO
        elif self.cellType == 'triangle': pass #TODO

    def giveBirth (self, percent=0.2, mode='rand'):
        # TODO: improve via template-based initiation, such as glider
        if mode == 'rand':
            for i in np.arange(percent*self.size[0]*self.size[1]):
                c = np.random.random_integers(self.size[0]-1)
                r = np.random.random_integers(self.size[1]-1)
                self.grid[c][r] = 1
        elif mode == 'glider':
            pass
        

    def calcNeighborSum(self):
        if self.cellType == 'square':
            '''
            instead of adding values of the neighbors one by one,
            the image is shifted and sum up shifted images into "neighborSum".
            the result will be the summation of neighbors, plus the value of cell itself.
            that's why the "neighborSum" is initiated with negative of self.grid'''
            
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

        elif self.cellType == 'hexagon': pass #TODO
        elif self.cellType == 'triangle': pass #TODO

    def conway(self, born=3, stayAlive=[2,3]):
        # TODO: improve speed
        for r in range(self.size[0]):
            for c in range(self.size[1]):
                if (self.grid[r,c] == 0) and (self.neighborSum[r,c]==born):
                    self.grid[r,c]=1.
                elif (self.grid[r,c] == 1) and (self.neighborSum[r,c] in stayAlive):
                    pass
                else:
                    self.grid[r,c]=0.

    def iterate(self):
        self.calcNeighborSum()
        if self.cellType == 'square':
            self.rule()
        elif self.cellType == 'hexagon': pass #TODO
        elif self.cellType == 'triangle': pass #TODO







# ###########################################
# myAut = CellularAutomata(gridSize=[200,200])
# myAut.giveBirth()


# import matplotlib.pyplot as plt
# rows,cols = 2,2
# fig = plt.figure(figsize=(cols*6,rows*6))
# axes = [plt.subplot2grid((rows, cols), (r, c), rowspan=1, colspan=1, axisbg = 'w')
#         for c in range(cols) for r in range(rows)]

# img = myAut.grid
# axes[0].imshow(img, cmap='gray', origin='lower')
# for i in range(10):    myAut.iterate()
# img = myAut.grid
# axes[1].imshow(img, cmap='gray', origin='lower')
# for i in range(10):    myAut.iterate()
# img = myAut.grid
# axes[2].imshow(img, cmap='gray', origin='lower')
# for i in range(10):    myAut.iterate()
# img = myAut.grid
# axes[3].imshow(img, cmap='gray', origin='lower')

# plt.show()


