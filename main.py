import pygame
import sys
import pygame_menu
from pygame_menu import themes
import game_logic
from game_logic import *
from board import Board
from tile import *


pygame.init()

WIDTH, HEIGHT = 800, 600
_volume = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mahjong Start")

clock = pygame.time.Clock()

tile=Tile('red','dot 7',Vector(0,0,0))
generate_tile_image(tile)

class Rules:
    def __init__(self):
        player_mode=' '
        difficulty=' '

    def set_player_mode(self,_new_mode,_val):
        self.player_mode = _new_mode
        print(_val)

    def set_difficulty(self,_new_diff,_val):
        self.difficulty = _new_diff
        print(_val)

rules=Rules()

def start_game_menu():
    game_menu=pygame_menu.Menu('Select game options:',WIDTH,HEIGHT,theme=themes.THEME_GREEN)
    game_menu.add.selector('Select mode: ',[('Single player',1),('vs Computer',2)],onchange=rules.set_player_mode)
    game_menu.add.selector('Select difficulty level: ',[('easy',1),('normal',2),('hard',3)],onchange=rules.set_difficulty)
    game_menu.add.button('Start the game', game)

    '''while True:
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
        clock.tick(60)'''
    mainmenu._open(game_menu)

def creators_menu():
    creators = pygame_menu.Menu('Creator of the game', WIDTH,HEIGHT,theme=themes.THEME_BLUE)
    creators.add.label("Emilia Miaskiewicz")
    mainmenu._open(creators)

def change_volume(value):
    global _volume
    _volume = value

def options_menu():
    options = pygame_menu.Menu('Options', WIDTH, HEIGHT, theme=themes.THEME_BLUE)
    options.add.range_slider('Volume',default=_volume,range_values=[int(0),int(100)],increment=int(1),width=250,onchange=change_volume)
    mainmenu._open(options)

mainmenu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_game_menu)
mainmenu.add.button('Creator', creators_menu)
mainmenu.add.button('Options', options_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(screen)

    pygame.display.update()


'''def main():
    board = Board()

    print(board.find_on_board(Vector(45,4,2)))


main()'''

#na koniec programu czyscic folder generated files???
#moze zostawic do nastepnych programow jako pamiec podreczna???