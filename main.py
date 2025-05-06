import pygame
import sys

from board import Board
from tile import *


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mahjong Start")

font = pygame.font.SysFont('comicsansms', 48)
clock = pygame.time.Clock()

#print(pygame.font.get_fonts())

def draw_text(text, font, color, surface, x, y):
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=(x, y))
    surface.blit(txt, rect)
    return rect

def main_menu():
    while True:
        screen.fill((30, 30, 60))
        start_button = draw_text("Start", font, (255, 255, 255), screen, WIDTH//2, HEIGHT//2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_loop()

        pygame.display.flip()
        clock.tick(60)

def game_loop():
    while True:
        screen.fill((60, 120, 90))  # tu bedzie gra

        quit_button = draw_text("Quit", font, (255, 255, 255), screen, WIDTH//2, HEIGHT//2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.collidepoint(event.pos):
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

main_menu()


'''def main():
    board = Board()

    print(board.find_on_board(Vector(45,4,2)))


main()'''

#na koniec programu czyscic folder generated files???
#moze zostawic do nastepnych programow jako pamiec podreczna???