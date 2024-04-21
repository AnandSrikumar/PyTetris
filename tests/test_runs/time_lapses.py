import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Elapsed Time")

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up colors
WHITE = (255, 255, 255)

# Initialize clock
clock = pygame.time.Clock()

# Main game loop
def main():
    start_time = pygame.time.get_ticks()  # Get start time in milliseconds
    elapsed_seconds = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Calculate elapsed time in seconds
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        elapsed_seconds = elapsed_time // 1000  # Convert milliseconds to seconds
        
        # Reset elapsed seconds to 0 every 5 seconds
        if elapsed_seconds % 5 == 0 and elapsed_seconds != 0:
            elapsed_seconds = 0
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Render elapsed time as text
        time_text = font.render("Elapsed Time: {} seconds".format(elapsed_seconds), True, (0, 0, 0))
        screen.blit(time_text, (50, 50))
        
        # Update the display
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
