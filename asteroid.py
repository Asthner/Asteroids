from circleshape import CircleShape
import pygame, constants, random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20.0, 50.0)
            vel1 = self.velocity.rotate(angle)
            vel2 = self.velocity.rotate(-angle)
            rad = self.radius - constants.ASTEROID_MIN_RADIUS
            aster1 = Asteroid(self.position.x, self.position.y, rad)
            aster1.velocity = vel1 * 1.2
            aster2 = Asteroid(self.position.x, self.position.y, rad)
            aster2.velocity = vel2 * 1.2