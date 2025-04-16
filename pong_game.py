import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 10

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Paddle positions
paddle1_y = paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball position
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED

    # Move ball
    ball_x += BALL_SPEED_X
    ball_y += BALL_SPEED_Y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        BALL_SPEED_Y *= -1

    # Ball collision with paddles
    if (ball_x <= PADDLE_WIDTH and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT) or \
       (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT):
        BALL_SPEED_X *= -1

    # Ball out of bounds
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        BALL_SPEED_X, BALL_SPEED_Y = random.choice([-5, 5]), random.choice([-5, 5])

    # Fill screen
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()