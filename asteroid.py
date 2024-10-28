from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y , radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color = "white", center =  self.position, radius = self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            smallv = self.velocity.rotate(-random_angle)
            bigv = self.velocity.rotate(random_angle)
            newradius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, newradius)
            ast2 = Asteroid(self.position.x, self.position.y, newradius)
            ast1.velocity = smallv * 1.2
            ast2.velocity = bigv * 1.2