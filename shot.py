from circleshape import CircleShape
import pygame, constants

class Shot(CircleShape):

    def __init__(self, x, y, v):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = v

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt