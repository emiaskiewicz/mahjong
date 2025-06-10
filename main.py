import pygame
import sys
import pygame_menu
from pygame_menu import themes
import rules_and_logic
from tile import *


pygame.init()

WIDTH, HEIGHT = 1300, 700

_volume = 100
sets=[("Kopiec",1),("Odwrocony kopiec",2)]
difficulties=[('easy','easy'),('normal','normal'),('hard','hard')]
game_modes=[('Single player','Single player'),('vs Computer','vs Computer')]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mahjong Start")

clock = pygame.time.Clock()

'''tile=Tile('red','dragon green',Vector(0,0,0))
generate_tile_image(tile)'''

class Rules:
    player_name='username'
    game_mode = ' '
    difficulty = ' '
    set_name = ' '

    def __init__(self):
        pass

    def set_player_name(self,_new_name):
        self.player_name=_new_name

    def set_game_mode(self, _new_mode, _val):
        self.game_mode = _new_mode
        print(_val)

    def set_difficulty(self,_new_diff,_val):
        self.difficulty = _new_diff
        print(_val)

    def set_gameSet(self,_new_name,_val):
        self.set_name = _new_name
        print(_val)

    def print_rules(self):
        return print(f"Info\nPlayer name: {self.player_name}\tGame mode: {self.game_mode}\t"
                     f"Difficulty: {self.difficulty}\tGame set: {self.set_name}")

    def save_rules(self,dict):
        self.rules=dict
        print(self.rules)


rules=Rules()

def start_game():
    game = rules_and_logic.Logic("asd")
    game.run_game_loop(screen)

def start_game_menu():
    game_menu=pygame_menu.Menu('Select game options:',WIDTH,HEIGHT,theme=themes.THEME_GREEN)
    game_menu.add.text_input('Name: ', default='username', maxchar=20,onchange=rules.set_player_name)
    game_menu.add.selector('Select mode: ',default=0, items=game_modes, onchange=rules.set_game_mode)
    game_menu.add.selector('Select difficulty level: ',default=0,items=difficulties,onchange=rules.set_difficulty)
    game_menu.add.dropselect("Select game set: ",items=sets,onchange=rules.set_gameSet)
    game_data = game_menu.get_input_data()
    rules.save_rules(game_data)
    game_menu.add.button('Start the game', start_game)


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




#na koniec programu czyscic folder generated files???
#moze zostawic do nastepnych programow jako pamiec podreczna???