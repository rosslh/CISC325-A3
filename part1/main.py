import matplotlib.pyplot as plt
from pylab import *
import canvas
import random
from boid import Boid


def main():
    numBoids = 10
    boids = []
    for _ in range(numBoids):
        boids.append(Boid(1, [random.randint(0, 10), random.randint(0, 10)], [
                     random.randint(0, 10), random.randint(0, 10)]))

    iterations = 10
    for i in range(iterations):
        for boid in boids:
            beforePos = boid.position[:]  # makes a shallow copy of the array
            bId = boid.id

            boid.update_position(boids)
            # print("Boid {} Before: {} After: {}".format(
            # boid.id, beforePos, boid.position))

    plotCoordinates(boidOnex, boidOney, boidTwox, boidTwoy)


main()
