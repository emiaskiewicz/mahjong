from PIL.ImageOps import scale
from PIL import Image

from board import Board
from tile import *
from ursina import *

#app = Ursina()

test_tile= Tile('blue','dot 7',Vector(0,0,0))

#app.run()

#funkcja do generowania wygladu kafelka
#nie jest pelna - trzeba dodac obrazek numerka
def generate_tile_image(tile):
    #jesli juz istnieje plik to break zeby pominac

    color_img = Image.open(f"assets_images/colors/{tile.color}.png").convert("RGBA")
    figure_img = Image.open(f"assets_images/figures/{tile.figure}.png").convert("RGBA")

    #if tile.figure in ['bamboo 1','bamboo 2','bamboo 3', 'bamboo 4']:
    x = 341 - figure_img.width // 2 - 36
    y = 438 - figure_img.height // 2 - 28
    color_img.paste(figure_img, (x, y), figure_img)


    out_path = "generated_tiles/" + tile.color + "_" + tile.figure + ".png"
    color_img.save(out_path)



generate_tile_image(test_tile)
'''def main():
    board = Board()

    print(board.find_on_board(Vector(45,4,2)))


main()'''

#na koniec programu czyscic folder generated files???
#moze zostawic do nastepnych programow jako pamiec podreczna???