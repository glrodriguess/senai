import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Forca")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fonte
font = pygame.font.SysFont(None, 55)

# Palavras para o jogo
words = ["python", "pygame", "programacao", "desenvolvimento", "jogo"]

# Função para desenhar a forca
def draw_hangman(tries):
    if tries == 6:
        pygame.draw.line(screen, RED, (150, 200), (150, 300), 5)  # Poste
        pygame.draw.line(screen, RED, (100, 300), (200, 300), 5)  # Base
        pygame.draw.line(screen, RED, (150, 200), (100, 200), 5)  # Topo
        pygame.draw.line(screen, RED, (150, 200), (150, 150), 5)  # Braço
    if tries <= 5:
        pygame.draw.circle(screen, RED, (150, 150), 20, 5)  # Cabeça
    if tries <= 4:
        pygame.draw.line(screen, RED, (150, 170), (150, 230), 5)  # Corpo
    if tries <= 3:
        pygame.draw.line(screen, RED, (150, 230), (130, 270), 5)  # Braço esquerdo
    if tries <= 2:
        pygame.draw.line(screen, RED, (150, 230), (170, 270), 5)  # Braço direito
    if tries <= 1:
        pygame.draw.line(screen, RED, (150, 270), (130, 310), 5)  # Perna esquerda
    if tries == 0:
        pygame.draw.line(screen, RED, (150, 270), (170, 310), 5)  # Perna direita

# Função para desenhar a palavra oculta
def draw_word(word, guessed_letters):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    text = font.render(display_word, True, BLACK)
    screen.blit(text, (300, 400))

# Função principal do jogo
def main():
    word = random.choice(words).upper()
    guessed_letters = set()
    tries = 6
    guessed = False

    while True:
        screen.fill(WHITE)
        draw_hangman(tries)
        draw_word(word, guessed_letters)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                letter = pygame.key.name(event.key).upper()
                if letter.isalpha() and len(letter) == 1:
                    if letter in word:
                        guessed_letters.add(letter)
                        if set(word) == guessed_letters:
                            guessed = True
                    else:
                        tries -= 1

        if tries == 0:
            print(f"Você perdeu! A palavra era: {word}")
            pygame.quit()
            sys.exit()
        if guessed:
            print(f"Você ganhou! A palavra era: {word}")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()