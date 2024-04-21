import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Set the size of each block
BLOCK_SIZE = 40

# Set the screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the I-shaped Tetrimino
I_SHAPE = [
    [[1], [1], [1], [1]],  # Original orientation
    [[1, 1, 1, 1]],         # 90-degree clockwise rotation
    [[1], [1], [1], [1]],   # 180-degree clockwise rotation
    [[1, 1, 1, 1]]          # 270-degree clockwise rotation (or 90-degree counter-clockwise rotation)
]

# Define the S-shaped Tetrimino
S_SHAPE = [
    [[0, 1, 1],
     [1, 1, 0]],            # Original orientation
    [[1, 0],
     [1, 1],
     [0, 1]],               # 90-degree clockwise rotation
    [[0, 1, 1],
     [1, 1, 0]],            # 180-degree clockwise rotation
    [[1, 0],
     [1, 1],
     [0, 1]]                # 270-degree clockwise rotation (or 90-degree counter-clockwise rotation)
]

# Define the Z-shaped Tetrimino
Z_SHAPE = [
    [[1, 1, 0],
     [0, 1, 1]],            # Original orientation
    [[0, 1],
     [1, 1],
     [1, 0]],               # 90-degree clockwise rotation
    [[1, 1, 0],
     [0, 1, 1]],            # 180-degree clockwise rotation
    [[0, 1],
     [1, 1],
     [1, 0]]                # 270-degree clockwise rotation (or 90-degree counter-clockwise rotation)
]

# Define a function to draw the Tetrimino
def draw_shape(x, y, shape):
    for row_index, row in enumerate(shape):
        for col_index, block in enumerate(row):
            if block == 1:
                pygame.draw.rect(screen, GRAY, (x + col_index * BLOCK_SIZE, y + row_index * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BLACK, (x + col_index * BLOCK_SIZE, y + row_index * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# Main loop
running = True
current_rotation_I = 0
current_rotation_S = 0
current_rotation_Z = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Rotate the I-shaped Tetrimino
                current_rotation_I = (current_rotation_I + 1) % 4
                # Rotate the S-shaped Tetrimino
                current_rotation_S = (current_rotation_S + 1) % 4
                # Rotate the Z-shaped Tetrimino
                current_rotation_Z = (current_rotation_Z + 1) % 4

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the I-shaped Tetrimino at coordinates (100, 100)
    draw_shape(100, 100, I_SHAPE[current_rotation_I])

    # Draw the S-shaped Tetrimino at coordinates (300, 100)
    draw_shape(300, 100, S_SHAPE[current_rotation_S])

    # Draw the Z-shaped Tetrimino at coordinates (500, 100)
    draw_shape(500, 100, Z_SHAPE[current_rotation_Z])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
