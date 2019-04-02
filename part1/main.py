import matplotlib.pyplot as plt
from pylab import *
import random
from boid import Boid
from tkinter import *
import time
import random

canvasSize = 800
boidSize = 20


def main():
    numBoids = 15
    boids = []
    for i in range(numBoids):
        boids.append(Boid(i, [random.randint(-20, 40), random.randint(-20, 40)],
                          [random.randint(30, 90), random.randint(30, 90)], canvasSize, boidSize))

    gui, canvas, ovals = drawCanvas(canvasSize, boids)

    windVector = [0, 0]
    windArrow = None
    windArrowOptions = {
        'width': 5,
        'arrowshape': (25, 30, 13)
    }

    iterations = 200
    try:
        for i in range(iterations):
            if i > iterations / 3:  # start wind 1/3 through simulation
                windVector = [sin(i / 10) * 30,  0]
                if windArrow is not None:
                    canvas.delete(windArrow)
                windArrow = createWindArrow(
                    canvas, windVector, canvasSize / 2, 40, windArrowOptions)
            for boid in boids:
                boid.update_position(boids, windVector)
                assert(boid.position[0] <
                       canvasSize and boid.position[1] < canvasSize)
                moveTo(canvas, ovals[boid.id],
                       boid.position[0], boid.position[1])
            time.sleep(.15)
            gui.update()
    except KeyboardInterrupt:  # close canvas in case of program quit
        gui.destroy()
    gui.title("test")
    gui.destroy()
    gui.mainloop()


def createWindArrow(canvas, windVector, x, y, options):
    length = max(abs(windVector[0]) * 5, 20)
    left = x - length
    right = x + length
    windArrow = None
    if windVector[0] > 0:
        windArrow = canvas.create_line(
            left, y, right, y, arrow=LAST, **options)
    else:
        windArrow = canvas.create_line(
            left, y, right, y, arrow=FIRST, **options)
    return windArrow


def moveTo(canvas, oval, x, y):
    currentCoords = canvas.coords(oval)
    currentX = (currentCoords[0] + currentCoords[2]) // 2
    currentY = (currentCoords[1] + currentCoords[3]) // 2

    xDiff = x - currentX
    yDiff = y - currentY

    canvas.move(oval, xDiff, yDiff)


def drawCanvas(boundary, initialBoids):
    gui = Tk()
    gui.geometry("{}x{}".format(int(boundary*1.5), int(boundary*1.5)))
    canvas = Canvas(gui, width=boundary, height=boundary, background="#fafafa")
    canvas.pack()
    ovals = {}
    for i, boid in enumerate(initialBoids):
        oval = canvas.create_oval(
            boid.position[0], boid.position[1], boid.position[0] + boidSize, boid.position[1] + boidSize, fill='red')
        ovals[i] = oval
    return gui, canvas, ovals


main()
