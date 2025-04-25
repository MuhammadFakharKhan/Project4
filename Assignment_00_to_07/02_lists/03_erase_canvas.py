import pygame
import asyncio
import platform

# Constants
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
ERASER_SIZE = 30
FPS = 60

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Eraser Canvas")

# Create grid to store cell colors
grid = [[BLUE for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Eraser properties
eraser_rect = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)
is_erasing = False

def setup():
    screen.fill(WHITE)
    draw_grid()

def draw_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[row][col], 
                           (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            # Draw grid lines
            pygame.draw.rect(screen, BLACK, 
                           (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def update_loop():
    global is_erasing, eraser_rect
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                is_erasing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_erasing = False
    
    # Update eraser position to follow mouse
    mouse_pos = pygame.mouse.get_pos()
    eraser_rect.center = mouse_pos
    
    # Erase cells if eraser is active
    if is_erasing:
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if eraser_rect.colliderect(cell_rect):
                    grid[row][col] = WHITE
    
    # Redraw everything
    screen.fill(WHITE)
    draw_grid()
    
    # Draw eraser (semi-transparent red rectangle)
    eraser_surface = pygame.Surface((ERASER_SIZE, ERASER_SIZE), pygame.SRCALPHA)
    eraser_surface.fill((255, 0, 0, 128))  # Red with 50% opacity
    screen.blit(eraser_surface, eraser_rect.topleft)
    
    pygame.display.flip()

async def main():
    setup()
    while True:
        update_loop()
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())