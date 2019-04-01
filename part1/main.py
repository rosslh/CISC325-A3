import matplotlib.pyplot as plt
from pylab import *
import random
from boid import Boid
from tkinter import *
import time
import random

canvasSize = 1000


def main():
    numBoids = 1
    boids = []
    for i in range(numBoids):
        boids.append(Boid(i, [0, 0], [10, 10], canvasSize))

    gui, canvas, ovals = drawCanvas(canvasSize, boids)
    iterations = 10
    for i in range(iterations):
        boidSnapshot = boids[:]
        for boid in boids:
            print(boid.id, boid.position, boid.velocity)
            bId = boid.id
            boid.update_position(boidSnapshot)
            assert(boid.position[0] <
                   canvasSize and boid.position[1] < canvasSize)
            canvas.move(ovals[boid.id], boid.velocity[0], boid.velocity[1])
            gui.update()
            time.sleep(.1)
        # display(boids)
    gui.title("test")
    gui.after(5000, gui.destroy)
    gui.mainloop()


def drawCanvas(boundary, initialBoids):
    gui = Tk()
    gui.geometry("{}x{}".format(int(boundary*1.5), int(boundary*1.5)))
    canvas = Canvas(gui, width=boundary, height=boundary)
    canvas.pack()
    boidSize = 20
    ovals = {}
    for i, boid in enumerate(initialBoids):
        oval = canvas.create_oval(
            boid.position[0], boid.position[1], boid.position[0] + boidSize, boid.position[1] + boidSize, fill='red')
        ovals[i] = oval
    return gui, canvas, ovals


main()
