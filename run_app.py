import pygame
from main import mainmenu

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Mahjong")
    mainmenu(screen)
    pygame.quit()

if __name__ == "__main__":
    main()