import os

TILE_WIDTH, TILE_HEIGHT = 80, 100
Z_OFFSET_X, Z_OFFSET_Y = 8, 5

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

def draw_board(screen, board, highlited_tiles=[]):
    import pygame

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

        if tile.position in highlited_tiles:
            tile_img = lighten_image(tile_img)

        screen.blit(tile_img, (screen_x, screen_y))