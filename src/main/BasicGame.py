import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Movement")

# Define player variables
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
player_speed = 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of keys
    keys = pygame.key.get_pressed()

    # Update player position based on key presses
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Boundary check
    player_x = max(0, min(player_x, SCREEN_WIDTH - 20))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - 20))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 20, 20))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()