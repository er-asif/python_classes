import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Basket
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 50
basket_speed = 7

# Ball
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move ball
    ball_y += ball_speed

    # Collision check
    if (basket_y < ball_y + ball_radius < basket_y + basket_height and
        basket_x < ball_x < basket_x + basket_width):
        score += 1
        ball_y = 0
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    # Missed ball
    if ball_y > HEIGHT:
        running = False

    # Draw basket and ball
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
print("Game Over! Final Score:", score)
