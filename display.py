import os
import pygame
import random

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_MARGIN = 20

TILE_WIDTH, TILE_HEIGHT = 60, 80
Z_OFFSET_X, Z_OFFSET_Y = 6, 6



def draw_hint_button(screen):
    font = pygame.font.Font(None, 36)
    button_width,button_height = 100,50
    button_x,button_y = 20,20

    hint_button = pygame.Rect(button_x, button_y, button_width, button_height)

    pygame.draw.rect(screen, BLUE, hint_button)

    hint_text = font.render("Hint", True, WHITE)
    screen.blit(hint_text, (hint_button.x + (hint_button.width - hint_text.get_width()) // 2,
                            hint_button.y + (hint_button.height - hint_text.get_height()) // 2))

    return hint_button

def draw_delete_button(screen):
    font = pygame.font.Font(None, 32)
    button_width = 100
    button_height = 50
    button_x = screen.get_width() - 20 - button_width
    button_y = screen.get_height() - 20 - button_height

    delete_button = pygame.Rect(button_x, button_y, button_width, button_height)

    pygame.draw.rect(screen, BLUE, delete_button)

    delete_text = font.render("Remove", True, WHITE)
    screen.blit(delete_text, (delete_button.x + (delete_button.width - delete_text.get_width()) // 2,
                            delete_button.y + (delete_button.height - delete_text.get_height()) // 2))

    return delete_button

def end_game_message(screen):
    font = pygame.font.Font(None, 36)
    window_width = 400
    window_height = 200
    window_x = (screen.get_width() - window_width) // 2
    window_y = (screen.get_height() - window_height) // 2
    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, WHITE, (window_x, window_y, window_width, window_height))
    pygame.draw.rect(screen, BLACK, (window_x, window_y, window_width, window_height), 2)

    text = font.render("No moves available!", True, BLACK)
    screen.blit(text, (window_x + (window_width - text.get_width()) // 2, window_y + 20))

    quit_button = pygame.Rect(window_x + (window_width-BUTTON_WIDTH)//2, window_y + window_height - BUTTON_MARGIN - BUTTON_HEIGHT,
                              BUTTON_WIDTH, BUTTON_HEIGHT)
    shuffle_button = pygame.Rect(window_x + (window_width - BUTTON_WIDTH) // 2,
                                 window_y + window_height - 2 * BUTTON_MARGIN - 2 * BUTTON_HEIGHT, BUTTON_WIDTH,
                                 BUTTON_HEIGHT)

    pygame.draw.rect(screen, RED, quit_button)
    pygame.draw.rect(screen, GREEN, shuffle_button)

    quit_text = font.render("Exit game", True, BLACK)
    shuffle_text = font.render("Shuffle board", True, BLACK)

    screen.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2,
                            quit_button.y + (quit_button.height - quit_text.get_height()) // 2))
    screen.blit(shuffle_text, (shuffle_button.x + (shuffle_button.width - shuffle_text.get_width()) // 2,
                               shuffle_button.y + (shuffle_button.height - shuffle_text.get_height()) // 2))

    pygame.display.flip()

    return quit_button, shuffle_button

def get_screen_position(position,offset_x, offset_y):
    x = position.x * TILE_WIDTH - position.z * Z_OFFSET_X+offset_x
    y = position.y * TILE_HEIGHT - position.z * Z_OFFSET_Y+offset_y
    return x, y

def lighten_image(image,factor=1.5):
    import pygame
    image = image.convert_alpha()
    image_array = pygame.surfarray.pixels3d(image)
    image_array = image_array * factor
    image_array = image_array.clip(0, 255)

    return pygame.surfarray.make_surface(image_array)

def handle_click(screen,board,pos,highlited_tiles,logic):
    screen_width, screen_height = screen.get_size()
    board_width, board_height = board.get_board_size()

    offset_x = (screen_width - board_width) // 2
    offset_y = (screen_height - board_height) // 2

    for tile in board.tiles_list:
        screen_x, screen_y = get_screen_position(tile.position, offset_x, offset_y)

        if screen_x <= pos[0] <= screen_x + TILE_WIDTH and screen_y <= pos[1] <= screen_y + TILE_HEIGHT:
            if tile not in highlited_tiles and board.is_available(tile) and len(highlited_tiles)<3:
                highlited_tiles.append(tile)
            elif tile in highlited_tiles:
                highlited_tiles.remove(tile)
            else:
                continue



def draw_board(screen, board, highlited_tiles=[]):
    screen_width, screen_height = screen.get_size()
    board_width, board_height = board.get_board_size()

    offset_x = (screen_width - board_width) // 2
    offset_y = (screen_height - board_height) // 2

    for tile in board.tiles_list:
        img_name= tile.get_tile_name()+".png"
        img_path = os.path.join("generated_tiles",img_name)
        try:
            tile_img = pygame.image.load(img_path).convert_alpha()
        except:
            continue

        screen_x, screen_y = get_screen_position(tile.position,offset_x,offset_y)

        if len(highlited_tiles) >0:
            if tile.position in [highlited_tile.position for highlited_tile in highlited_tiles]:
                tile_img = lighten_image(tile_img)


        screen.blit(tile_img, (screen_x, screen_y))