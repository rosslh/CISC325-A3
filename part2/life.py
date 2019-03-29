import numpy as np
import math as m
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from copy import copy, deepcopy

def readFile(filename):
    with open(filename) as f:
        file = f.readlines()
    board = []
    nsteps = str(file[0])
    for row in file[1:]:

        board.append([int(x) for x in list(row.rstrip('\n'))])
    return nsteps, board

def animate(vals):
    fig, axes = plt.subplots()
    def update_plot(i):
        print(i)
        axes.clear()
        im = axes.pcolormesh(vals[i], cmap="Greys", vmin=0, vmax=1)
        return axes
    ani = FuncAnimation(fig, update_plot, frames=len(vals), interval=500)
    plt.show()

def num_neighbours(x, y):
    total = 0
    if y > 0:
        total += board[y-1][x]
    if y < len(board[0])-1:
        total += board[y+1][x]
    if x > 0:
        total += board[y][x-1]
        if y > 0:
            total += board[y-1][x-1]
        if y < len(board)-1:
            total += board[y+1][x-1]
    if x < len(board[0])-1:
        total += board[y][x+1]
        if y > 0:
            total += board[y-1][x+1]
        if y < len(board[0])-1:
            total += board[y+1][x+1]
    return total

def step(board):
    next = deepcopy(board)
    for y in range(len(board)):
        for x in range(len(board[0])):
            n = num_neighbours(x, y)
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
next = step(board)
#nnext = step(next)
vals = [board, next]
animate(vals)
