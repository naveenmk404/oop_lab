import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shapes Drawing")

# Define colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw shapes
    # Polygon
    pygame.draw.polygon(screen, BLUE, [(146, 0), (291, 106), (236, 277), (56, 277), (0, 106)])

    # Line
    pygame.draw.line(screen, GREEN, (60, 300), (120, 300), 4)

    # Circle
    pygame.draw.circle(screen, GREEN, (300, 50), 20)

    # Ellipse
    pygame.draw.ellipse(screen, BLACK, (300, 250, 40, 80), 1)

    # Rectangle
    pygame.draw.rect(screen, BLACK, (150, 300, 100, 50))

    # Update the display
    pygame.display.flip()
