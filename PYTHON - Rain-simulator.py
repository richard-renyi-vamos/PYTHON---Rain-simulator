import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Simulator")

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# Raindrop class
class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-20, HEIGHT - 20)

    def update(self):
        self.rect.y += random.randint(4, 10)  # Speed of the raindrop
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(-20, -1)
            self.rect.x = random.randint(0, WIDTH)

# Create a group for raindrops
raindrops = pygame.sprite.Group()

# Generate raindrops
for _ in range(100):  # Adjust the number for more/less rain
    raindrop = Raindrop()
    raindrops.add(raindrop)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update raindrops
    raindrops.update()

    # Draw everything
    screen.fill(BLACK)  # Clear the screen
    raindrops.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame
pygame.quit()
