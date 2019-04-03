import numpy as np
import math as m
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from copy import copy, deepcopy

def readFile(filename):
    '''
        Reads in the starting information from a file
    '''
    with open(filename) as f:
        file = f.readlines()
    board = []
    nsteps = int(file[0])
    for row in file[1:]:

        board.append([int(x) for x in list(row.rstrip('\n'))])
    return nsteps, board

def writeOutput(frames, filename):
    '''
        Outputs the frames to a file
    '''
    with open(filename,'w') as out:
        for ind in range(len(frames)):
            out.write('Generation '+str(ind)+"\n")
            for row in frames[ind]:
                line = ''.join(str(x) for x in row)+"\n"
                out.write(line)

def animate(frames):
    '''
        Animates the frames using matplotlib
    '''
    fig, axes = plt.subplots()
    def updatePlot(i):
        axes.clear()
        im = axes.pcolormesh(frames[i], cmap="Greys", vmin=0, vmax=1)
        ax = plt.gca()
        ax.invert_yaxis()
        return axes
    ani = FuncAnimation(fig, updatePlot, frames=len(frames), interval=500)
    plt.show()

def numNeighbours(x, y, board):
    '''
        Calculates the number of neighbours for a given location in the board
    '''
    total = 0
    if y > 0:
        total += board[y-1][x] # up
    if y < len(board)-1:
        total += board[y+1][x] # down
    if x > 0:
        total += board[y][x-1] # left
        if y > 0:
            total += board[y-1][x-1] # up-left diagonal
        if y < len(board)-1:
            total += board[y+1][x-1] # down-left diagonal
    if x < len(board[0])-1:
        total += board[y][x+1] # right
        if y > 0:
            total += board[y-1][x+1] # up-right
        if y < len(board)-1:
            total += board[y+1][x+1] # down-right
    return total

def step(board):
    '''
        Finds the next frame in the game of life
    '''
    next = deepcopy(board)
    print(len(board))
    print(len(board[0]))
    for y in range(len(board)):
        for x in range(len(board[0])):
            n = numNeighbours(x, y, board)
            alive = board[y][x]
            if alive and n < 2:
                next[y][x] = 0 # Dies :(
            elif alive and n > 3:
                next[y][x] = 0 # Dies :(
            elif alive and (n == 2 or n == 3):
                pass # survives :)
            elif not alive and n == 3:
                next[y][x] = 1
    return next

n, board = readFile("inLife.txt")
next = board
frames = [board]
for i in range(n):
    next = step(next)
    if i==0:
        print(board)
    frames.append(next)
writeOutput(frames, "outLife.txt")
animate(frames)
