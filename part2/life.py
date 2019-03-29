import numpy as np
import math as m
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(vals):
    fig, axes = plt.subplots()
    def update_plot(i):
        print(i)
        axes.clear()
        im = axes.pcolormesh(vals[i], cmap="Greys", vmin=0, vmax=1)
        return axes
    ani = FuncAnimation(fig, update_plot, frames=len(vals), interval=1000)
    plt.show()

vals = [ [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]],
         [[0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]],
         [[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]] ]

animate(vals)
