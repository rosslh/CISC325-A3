import math


class Boid:
    def __init__(self, id, velocity, position, boundary, size=0):
        self.id = id
        self.size = size
        self.boundary = boundary
        self.position = position  # x, y
        self.velocity = velocity  # x, y

    def update_position(self, boids, windVector):
        self.rule1(boids)
        self.rule2(boids)
        self.rule3(boids)

        self.applyWind(windVector)

        self._limitVelocity()

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        self.position[0] %= self.boundary
        self.position[1] %= self.boundary

    '''
        Use the sigmoid function to taper off velocity if it is accelerating out 
        of control due to the emergent behaviour of the system
    '''

    def applyWind(self, windVector):
        print(windVector)
        self.velocity[0] += windVector[0]
        self.velocity[1] += windVector[1]

    def _limitVelocity(self):
        velocityRange = 150  # max value is velocity range/2,
        self.velocity[0] = self._sigmoid(self.velocity[0], velocityRange)
        self.velocity[1] = self._sigmoid(self.velocity[1], velocityRange)

    def _sigmoid(self, x, velocityRange):
        div5 = velocityRange/5
        denominator = 1 + math.exp(-(1/div5) * x)
        fraction = (1/denominator)*velocityRange
        return fraction-(velocityRange/2)

    # moves boid to middle of center of mass
    def rule1(self, boids):
        # a vector representing the center of mass for the boid's neighbourhood
        centerOfMass = self.position[:]
        for boid in boids:
            if boid.id != self.id:
                centerOfMass[0] = centerOfMass[0] + boid.position[0]
                centerOfMass[1] = centerOfMass[1] + boid.position[1]
        centerOfMass[0] /= len(boids)  # average x pos of other boids
        centerOfMass[1] /= len(boids)  # average y pos of other boids
        self.velocity[0] += (centerOfMass[0] -
                             self.position[0]) / 100  # weighted 1/100
        self.velocity[1] += (centerOfMass[1] - self.position[1]) / 100

    # Keep boids small distance apart

    def rule2(self, boids):
        vector = [0, 0]
        for boid in boids:
            if boid.id != self.id:
                if self._inSameNeighborhood(boid):
                    # subtract x coordinates
                    vector[0] -= self.position[0]-boid.position[0]
                    # subtract y coordinates
                    vector[1] -= self.position[1]-boid.position[1]
        self.velocity[0] += vector[0]
        self.velocity[1] += vector[1]

    # Align boid velocities

    def rule3(self, boids):
        flockVelocity = self.velocity[:]
        for boid in boids:
            if self.id != boid.id:
                if self._inSameNeighborhood(boid):
                    flockVelocity[0] += boid.velocity[0]
                    flockVelocity[1] += boid.velocity[1]
        flockVelocity[0] /= len(boids) - 1 or 1
        flockVelocity[1] /= len(boids) - 1 or 1
        self.velocity[0] += (flockVelocity[0] -
                             self.velocity[0]) / 8  # weighted 1/8
        self.velocity[1] += (flockVelocity[1] - self.velocity[1]) / 8

    def _inSameNeighborhood(self, boid):
        return self._distance(boid) < 40

    def _distance(self, boid):
        position = boid.position
        x_dist = math.pow(self.position[0]-position[0], 2)
        y_dist = math.pow(self.position[1]-position[1], 2)
        # accounts for boid size
        return max(math.sqrt(x_dist+y_dist) - self.size, 0)
