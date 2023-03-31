import pygame
import random

# Define the display size
WIDTH = 400
HEIGHT = 400

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define variables
circle_radius = 10
circle_position = [int(WIDTH/2), int(HEIGHT/2)]
circle_direction = [3, 0]  # right direction initially
border_width = 10

# Define functions

def draw_circle(screen):
    pygame.draw.circle(screen, RED, circle_position, circle_radius)


def draw_border(screen, border_rect):
    pygame.draw.rect(screen, BLACK, border_rect, border_width)


def move_circle(border_rect):
    global circle_direction

    # Generate a random number between 0 and 1
    random_number = random.randint(3, 10)
    random_direction = random.randint(0, 1)
    direction = [-1, 1]

    # Check for collision with border
    if circle_position[0] - circle_radius < border_rect.left or circle_position[0] + circle_radius > border_rect.right:
        circle_direction[0] *= -1
        circle_direction[1] = random_number * direction[random_direction]
        

    if circle_position[1] - circle_radius < border_rect.top or circle_position[1] + circle_radius > border_rect.bottom:
        circle_direction[1] *= -1
        circle_direction[0] = random_number * direction[random_direction]

    # Move the circle
    circle_position[0] += (circle_direction[0])
    circle_position[1] += (circle_direction[1])


def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brownian Motion")

    border_rect = pygame.Rect(
        border_width, border_width, WIDTH - 2*border_width, HEIGHT - 2*border_width)

    # Main loop
    running = True
    clock = pygame.time.Clock()
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw the border and circle
        draw_border(screen, border_rect)
        draw_circle(screen)

        # Move the circle
        move_circle(border_rect)

        # Update the screen
        pygame.display.update()

        # Limit the frame rate
        clock.tick(60)

    # Quit pygame
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()