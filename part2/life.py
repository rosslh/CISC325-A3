import numpy as np
import math as m
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def readFile(filename):
    """
        Reads the grids from a text file.
        Saves them as 2D arrays
    """
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
    ani = FuncAnimation(fig, update_plot, frames=len(vals), interval=1000)
    plt.show()

def step(board):
    pass

n, board = readFile("inLife.txt")
vals = [board]
animate(vals)
