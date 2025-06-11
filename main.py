import pygame
import pygame_menu
from pygame_menu import themes
import rules_and_logic
from players import Player

pygame.init()

WIDTH, HEIGHT = 1300, 700

_volume = 100
sets=[("Kopiec",1),("Odwrocony kopiec",2),("Test",3)]
difficulties=[('easy','easy'),('normal','normal'),('hard','hard')]
game_modes=[('Single player','Single player'),('CPU vs CPU','CPU vs CPU'),('Player vs CPU','Player vs CPU')]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mahjong Start")

clock = pygame.time.Clock()

player1=Player()
Game_menu= None

def start_game():
    game_data = game_menu.get_input_data()
    print(game_data)
    player1.save_settings(game_data)
    game = rules_and_logic.Logic(player1)
    game.game_mode(screen)

def start_game_menu():
    global game_menu
    game_menu=pygame_menu.Menu(title='Select game options:',width=WIDTH,height=HEIGHT,theme=themes.THEME_GREEN)
    game_menu.add.text_input(title='Name: ', default='username', maxchar=20,textinput_id='Name',name='Name')
    game_menu.add.dropselect(title='Select mode: ', items=game_modes,dropselect_id='Game mode',name='Game mode')
    game_menu.add.dropselect(title='Select difficulty level: ', items=difficulties,dropselect_id='Difficulty',name='Difficulty')
    game_menu.add.dropselect(title='Select game set: ', items=sets,dropselect_id='Game set',name='Game set')
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