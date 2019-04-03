import matplotlib.pyplot as plt
from pylab import *
import random
from boid import Boid
from tkinter import *
import time
import random


def main():
    numBoids = 30
    boids = []
    gui, canvas, canvasSize = createCanvas()
    boidSize = canvasSize // 100

    for i in range(numBoids):
        accx, accy = random.randint(-4, 4), random.randint(-4, 4)
        # accx, accy = random.randint(-40, 40), random.randint(-40, 40)
        boids.append(Boid(i, [accx, accy],[random.randint(0, canvasSize), random.randint(0, canvasSize)], canvasSize))

    ovals = drawBoids(canvas, boids, canvasSize, boidSize)
    windArrow = None
    windSpeed = 0

    windArrowOptions = {
        'width': 5,
        'arrowshape': (25, 30, 13)
    }
    iterations = 1000
    try:
        for i in range(iterations):
            if i > iterations / 2:  # start wind halfway through simulation
                windSpeed = sin(i / 30) * 4
                if windArrow is not None:
                    canvas.delete(windArrow)
                canvas.create_text(
                    canvasSize / 2, 70, fill="black", font="Times 20 italic bold", text="WIND")
                windArrow = createWindArrow(
                    canvas, windSpeed, canvasSize / 2, 40, windArrowOptions)

            for boid in boids:
                boid.update_position(boids, windSpeed)
                # canvas.move(ovals[boid.id],boid.velocity[0],boid.velocity[1])
                moveTo(canvas, ovals[boid.id],
                       boid.position[0], boid.position[1])
            time.sleep(.1)
            gui.update()
    except KeyboardInterrupt:  # close canvas in case of program quit
        gui.destroy()
    gui.title("Boid Simulation")
    gui.destroy()
    gui.mainloop()


def createWindArrow(canvas, windSpeed, x, y, options):
    length = max(abs(windSpeed) * 30, 20)
    left = x - length
    right = x + length
    windArrow = None
    if windSpeed > 0:
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


def createCanvas():
    gui = Tk()
    canvasSize = int(gui.winfo_screenheight() * 0.9)
    gui.geometry("{}x{}".format(canvasSize, canvasSize))
    canvas = Canvas(gui, width=canvasSize,
                    height=canvasSize, background="#fafafa")
    canvas.pack()
    return gui, canvas, canvasSize


def drawBoids(canvas, boids, boundary, boidSize):
    ovals = {}
    # colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta"]
    for i, boid in enumerate(boids):
        oval = canvas.create_oval(
            boid.position[0], boid.position[1], boid.position[0] + boidSize, boid.position[1] + boidSize, fill="red")
        ovals[boid.id] = oval
    return ovals


main()
