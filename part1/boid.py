import math


class Boid:
    def __init__(self, id, velocity, position):
        self.id = id
        self.position = position  # x, y
        self.velocity = velocity  # x, y

    def update_position(self, boids):
        self.rule1(boids)
        self.rule2(boids)
        self.rule3(boids)
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    # moves boid to middle of center of mass
    def rule1(self, boids):
        vector = [0, 0]
        for boid in boids:
            if boid.id != self.id:
                vector[0] = vector[0] + boid.position[0]
                vector[1] = vector[1] + boid.position[1]
        vector[0] /= len(boids)  # average x pos of other boids
        vector[1] /= len(boids)  # average y pos of other boids
        self.velocity[0] += (vector[0] - self.position[0]) / 100
        self.velocity[1] += (vector[1] - self.position[1]) / 100

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
        vector = [0, 0]
        for boid in boids:
            if self.id != boid.id:
                if self._inSameNeighborhood(boid):
                    vector[0] = vector[0] + boid.velocity[0]
                    vector[1] = vector[1] + boid.velocity[1]
        vector[0] /= len(boids)
        vector[1] /= len(boids)
        self.velocity[0] += (vector[0] - self.position[0]) / 8
        self.velocity[1] += (vector[1] - self.position[1]) / 8

    def _inSameNeighborhood(self, boid):
        return self._distance(boid) < 100

    def _distance(self, boid):
        position = boid.position
        x_dist = math.pow(self.position[0]-position[0], 2)
        y_dist = math.pow(self.position[1]-position[1], 2)
        return math.sqrt(x_dist+y_dist)
