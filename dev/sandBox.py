# TODO! turning class automata to image is too time consuming!
# start from begining with an image, fuck class stuff!
# start with an image, next iteration will be stored in a new image and then
# will be stored in the original image

# TODO: mutations, some cells die or live randomely
# then find a structure and try to use mutation to converge to a desire pattern.

# TODO: extend the states from binary to more,
# use coloring to illustrate

# TODO: add desease or super Power to some cells who would behave diferently

# TODO: add number of iterations to play


########################################
class Rules:
    def __init__(self):
        pass

    def conway(self, cellState, neighborState, thrMin=2, thrMax=3):        
        if cellState==True:
            if thrMin <= neighborState[True] <= thrMax:
                return True
            else:
                return False

        elif cellState==False:
            if neighborState[True] == thrMax:
                return True
            else:
                return False

########################################
class Cell:
    def __init__(self, state=False):
        self.state = state
        self.neighborIdx = [] #the indices of neighbors
        self.neighborhood = {False:0 , True:0}
        
    def readNeighborhood(self,grid):
        states = [grid[r][c].state for (r,c) in self.neighborsIdx]
        for s in list(set(states)): self.neighborhood[s] = states.count(s)

    def tempUpdate(self, rule):
        self.stateTemp = rule(self.state, self.neighborhood)

    def update(self):
        self.state = self.stateTemp

########################################
class Automata:
    def __init__(self, size, rule, neighborhoodRange=1, gridType='square'):
        ## all internal variables
        self.size = size #(r,c)
        self.rule = rule # a function
        self.gridType = gridType
        self.neighborhoodRange = neighborhoodRange

        nr = self.neighborhoodRange
        row, col = self.size

        #generateGrid
        if self.gridType == 'square':
            self.grid = [ [Cell() for c in range(col)] for r in range(row) ]
        elif self.gridType == 'hexagon': pass #TODO
        elif self.gridType == 'triangle': pass #TODO
        
        # finding neighbors of each cell
        if self.gridType == 'square':
            for r in range(row):
                for c in range(col):
                    self.grid[r][c].neighborsIdx = [ [r_,c_]
                                                     for r_ in range(max(r-nr,0), min(r+nr+1,row))
                                                     for c_ in range(max(c-nr,0), min(c+nr+1,col)) ]
                    self.grid[r][c].neighborsIdx.remove([r,c])
        elif self.gridType == 'hexagon': pass #TODO
        elif self.gridType == 'triangle': pass #TODO

    def iterate(self):
        if self.gridType == 'square':
            # looking to the neighborhood and updating temporarily
            for r in range(self.size[0]):
                for c in range(self.size[1]):
                    self.grid[r][c].readNeighborhood(self.grid)
                    self.grid[r][c].tempUpdate(self.rule)

            # updating 
            for r in range(self.size[0]):
                for c in range(self.size[1]):
                    self.grid[r][c].update()
                    
        elif self.gridType == 'hexagon': pass #TODO
        elif self.gridType == 'triangle': pass #TODO
    

    def genImage(self):
        image = np.array([1. if self.grid[r][c].state else 0.0
                          for r in range(np.shape(self.grid)[0])
                          for c in range(np.shape(self.grid)[1])]).reshape(np.shape(self.grid))
        return image
        


    
####################################
import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.figure import Figure

Demo = True
if Demo:
    gridSize = [200,200]
    myAut = Automata(gridSize, Rules().conway)
    for i in range(10000):
        c = np.random.random_integers(gridSize[0]-1)
        r = np.random.random_integers(gridSize[1]-1)
        myAut.grid[c][r].state = True


if True:
    for i in range(10):
        myAut.iterate()
        print 'itr: ' , i

    rows,cols = 1,1
    fig = plt.figure(figsize=(cols*6,rows*6))
    axes = [plt.subplot2grid((rows, cols), (r, c), rowspan=1, colspan=1, axisbg = 'w')
            for c in range(cols) for r in range(rows)]
    axes[0].imshow(myAut.genImage(), cmap='gray', origin='lower')
    plt.show()




# x = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# print 'start'

# nr = 2
# y = np.zeros([x.shape[0]+2*nr,x.shape[1]+2*nr])
# y[nr:-nr,nr:-nr] = x

# ns = np.zeros([x.shape[0]+2*nr,x.shape[1]+2*nr])
# ns[nr:-nr,nr:-nr] = -x

# for r in np.arange(-nr,nr+1):
#     y_ = np.roll(y, r, axis=0)
#     for c in np.arange(-nr,nr+1):
#         ns +=  np.roll(y_, c, axis=1)

# ns = ns[nr:-nr,nr:-nr]

# print x
# print ns
