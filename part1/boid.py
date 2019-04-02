import math


class Boid:
    def __init__(self, id, velocity, position, boundary):
        self.id = id
        self.boundary = boundary
        self.position = position  # x, y
        self.velocity = velocity  # x, y
        self.topSpeed = 150
        self.neighbourhoodSize = boundary//35

    def update_position(self, boids, windSpeed):
        self.neighbourhood = self.getNeighbors(boids)

        self.rule1(boids)
        self.rule2()
        self.rule3()

        self.applyWind(windSpeed)

        self._limitVelocity()

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        self.position[0] %= self.boundary
        self.position[1] %= self.boundary

    def applyWind(self, windSpeed):
        self.velocity[0] += windSpeed

    '''
    Use the sigmoid function to taper off velocity if it is accelerating out 
    of control due to the emergent behaviour of the system
    '''

    def _limitVelocity(self):
        velocityRange = self.topSpeed*2  # max value is velocity range/2,
        self.velocity[0] = self._sigmoid(self.velocity[0], velocityRange)
        self.velocity[1] = self._sigmoid(self.velocity[1], velocityRange)

    def _sigmoid(self, x, velocityRange):
        div5 = velocityRange/5
        denominator = 1 + math.exp(-(1/div5) * x)
        fraction = (1/denominator)*velocityRange
        return fraction-(velocityRange/2)

    # moves boid to middle of center of mass
    def rule1(self, boids):
        # a vector representing the center of mass for all boids in flock
        centerOfMass = self.position[:]
        for boid in boids:
            centerOfMass[0] = centerOfMass[0] + boid.position[0]
            centerOfMass[1] = centerOfMass[1] + boid.position[1]
        # average x pos of other boids
        centerOfMass[0] /= len(boids) - 1 or 1
        # average y pos of other boids
        centerOfMass[1] /= len(boids) - 1 or 1
        self.velocity[0] += (centerOfMass[0] -
                             self.position[0]) / 100  # weighted 1/100
        self.velocity[1] += (centerOfMass[1] - self.position[1]) / 100

    # Keep boids small distance apart

    def rule2(self):
        vector = [0, 0]
        for boid in self.neighbourhood:
            vector[0] -= self.position[0]-boid.position[0]
            vector[1] -= self.position[1]-boid.position[1]
        self.velocity[0] += vector[0]
        self.velocity[1] += vector[1]

    # Align boid velocities

    def rule3(self):
        flockVelocity = self.velocity[:]
        for boid in self.neighbourhood:
            flockVelocity[0] += boid.velocity[0]
            flockVelocity[1] += boid.velocity[1]
        flockVelocity[0] /= len(self.neighbourhood) - 1 or 1
        flockVelocity[1] /= len(self.neighbourhood) - 1 or 1
        self.velocity[0] += (flockVelocity[0] -
                             self.velocity[0]) / 8  # weighted 1/8
        self.velocity[1] += (flockVelocity[1] - self.velocity[1]) / 8

    def getNeighbors(self, boids):
        return [boid for boid in boids if self._distance(boid) < self.neighbourhoodSize and boid.id != self.id]

    def _distance(self, boid):
        position = boid.position
        x_dist = math.pow(self.position[0]-position[0], 2)
        y_dist = math.pow(self.position[1]-position[1], 2)
        return math.sqrt(x_dist+y_dist)
