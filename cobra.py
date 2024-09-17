import pygame
import time
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 15

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Cria a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Cobrinha')

# Define a fonte
font_style = pygame.font.SysFont(None, 50)

# Função para mostrar mensagem na tela
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

# Função principal do jogo
def gameLoop():
    game_over = False
    game_close = False

    # Coordenadas iniciais da cobrinha
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    # Mudança de coordenadas
    x1_change = 0
    y1_change = 0

    # Comprimento da cobrinha
    snake_list = []
    length_of_snake = 1

    # Coordenadas da comida
    foodx = round(random.randrange(0, SCREEN_WIDTH - CELL_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - CELL_SIZE) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message("Você perdeu! Pressione Q para sair ou C para jogar novamente.", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -CELL_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = CELL_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -CELL_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = CELL_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)

        # Desenha a comida
        pygame.draw.rect(screen, GREEN, [foodx, foody, CELL_SIZE, CELL_SIZE])

        # Atualiza a posição da cobrinha
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Desenha a cobrinha
        for x in snake_list:
            pygame.draw.rect(screen, WHITE, [x[0], x[1], CELL_SIZE, CELL_SIZE])

        pygame.display.update()

        # Verifica se a cobrinha comeu a comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - CELL_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - CELL_SIZE) / 20.0) * 20.0
            length_of_snake += 1

        # Checa se a cobrinha colidiu consigo mesma
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        clock.tick(FPS)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()