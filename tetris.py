import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
CELL_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE
FPS = 10

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Cria a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# Define as formas das peças do Tetris
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

# Cores das peças
SHAPE_COLORS = [CYAN, MAGENTA, YELLOW, GREEN, RED, ORANGE, BLUE]

# Função para criar uma grade vazia
def create_grid():
    return [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Função para desenhar a grade
def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if grid[y][x]:
                pygame.draw.rect(screen, SHAPE_COLORS[grid[y][x] - 1], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Função para desenhar uma peça
def draw_shape(shape, color, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, ((offset[0] + x) * CELL_SIZE, (offset[1] + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Função para verificar se uma peça pode ser colocada na grade
def valid_space(shape, offset, grid):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + offset[0] < 0 or x + offset[0] >= GRID_WIDTH or y + offset[1] >= GRID_HEIGHT:
                    return False
                if grid[y + offset[1]][x + offset[0]]:
                    return False
    return True

# Função para adicionar uma peça à grade
def add_shape_to_grid(shape, offset, grid, color_index):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + offset[1]][x + offset[0]] = color_index + 1

# Função para remover linhas completas
def remove_lines(grid):
    lines_to_remove = [i for i, row in enumerate(grid) if all(cell for cell in row)]
    for i in lines_to_remove:
        grid.pop(i)
        grid.insert(0, [0] * GRID_WIDTH)
    return len(lines_to_remove)

# Função principal do jogo
def gameLoop():
    clock = pygame.time.Clock()
    grid = create_grid()
    shape = random.choice(SHAPES)
    shape_color = SHAPE_COLORS[SHAPES.index(shape)]
    shape_offset = [GRID_WIDTH // 2 - len(shape[0]) // 2, 0]
    fall_time = 0
    run = True

    while run:
        screen.fill(BLACK)
        draw_grid(grid)
        draw_shape(shape, shape_color, shape_offset)
        pygame.display.update()
        
        fall_speed = 1000 // FPS
        fall_time += clock.get_rawtime()
        if fall_time >= fall_speed:
            shape_offset[1] += 1
            if not valid_space(shape, shape_offset, grid):
                shape_offset[1] -= 1
                add_shape_to_grid(shape, shape_offset, grid, SHAPES.index(shape))
                remove_lines(grid)
                shape = random.choice(SHAPES)
                shape_color = SHAPE_COLORS[SHAPES.index(shape)]
                shape_offset = [GRID_WIDTH // 2 - len(shape[0]) // 2, 0]
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shape_offset[0] -= 1
                    if not valid_space(shape, shape_offset, grid):
                        shape_offset[0] += 1
                elif event.key == pygame.K_RIGHT:
                    shape_offset[0] += 1
                    if not valid_space(shape, shape_offset, grid):
                        shape_offset[0] -= 1
                elif event.key == pygame.K_DOWN:
                    shape_offset[1] += 1
                    if not valid_space(shape, shape_offset, grid):
                        shape_offset[1] -= 1
                elif event.key == pygame.K_UP:
                    rotated_shape = list(zip(*shape[::-1]))
                    if valid_space(rotated_shape, shape_offset, grid):
                        shape = rotated_shape
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        clock.tick(FPS)

if __name__ == "__main__":
    gameLoop()