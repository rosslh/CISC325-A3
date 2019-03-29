import matplotlib.pyplot as plt
from pylab import *
import random
from boid import Boid
from tkinter import *
import time
import random


def main():
    numBoids = 10
    boids = []
    for _ in range(numBoids):
        boids.append(Boid(1, [random.randint(0, 50), random.randint(0, 50)], [
                     random.randint(0, 50), random.randint(0, 50)]))

    iterations = 10
    for i in range(iterations):
        for boid in boids:
            beforePos = boid.position[:]  # makes a shallow copy of the array
            bId = boid.id

            boid.update_position(boids)
            # print("Boid {} Before: {} After: {}".format(
            # boid.id, beforePos, boid.position))

        display(boids)


def display(boids):
    gui = Tk()
    gui.geometry("400x400")
    gui.title("Boids")
    canvas = Canvas(gui, width=300, height=300, bg='white')
    canvas.pack()
    boidShapes = []
    boidSize = 20
    for boid in boids:
        boidShapes.append(canvas.create_oval(boid.position[0], boid.position[1],
                                             boid.position[0] + boidSize, boid.position[1] + boidSize, fill='red'))

    gui.after(1000, gui.destroy)
    gui.mainloop()


main()
