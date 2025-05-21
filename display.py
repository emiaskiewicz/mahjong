import os

TILE_WIDTH, TILE_HEIGHT = 80, 100
Z_OFFSET_X, Z_OFFSET_Y = 10, 10

def get_screen_position(position):
    x = position.x * TILE_WIDTH - position.z * Z_OFFSET_X
    y = position.y * TILE_HEIGHT - position.z * Z_OFFSET_Y
    return x, y

def draw_board(screen, board, highlited_tiles=[]):
    import pygame
    for tile in board.tiles_list:
        img_name= tile.color +"_"+ tile.figure +".png"
        img_path = os.path.join("generated_tiles",img_name)
        try:
            tile_img = pygame.image.load(img_path).convert_alpha()
        except:
            continue

        screen_x, screen_y = get_screen_position(tile.position)
        screen.blit(tile_img, (screen_x, screen_y))