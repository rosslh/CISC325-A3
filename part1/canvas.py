from tkinter import *
import time
from boid import Boid
import random


def main(boids):
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
    gui.mainloop()


numBoids = 10
boids = []
for _ in range(numBoids):
    boids.append(Boid(1, [random.randint(0, 100), random.randint(0, 100)], [
        random.randint(0, 100), random.randint(0, 100)]))


main(boids)
