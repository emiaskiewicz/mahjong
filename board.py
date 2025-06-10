from tile import *
import random
import os
import json

game_sets_path = os.path.join("game_sets", "uklady.json")

class Board:
    sets_data = None
    tiles_dict: dict[Vector, Tile] = {}  # dostep do kafelkow po pozycji - wyszukiwanie O(1)
    tiles_list = []

    def __init__(self, set_name):
        with open(game_sets_path, mode="r", encoding="utf-8") as file:
            self.sets_data = json.load(file)

        for set in self.sets_data["sets"]:
            if set["name"] == set_name:
                for pos in set["positions"]:
                    position = Vector(pos[0], pos[1], pos[2])
                    tile = Tile(
                        color=random.choice(colors),
                        figure=random.choice(figures),
                        position=position
                    )
                    generate_tile_image(tile)
                    self.tiles_dict[position] = tile
                    self.tiles_list.append(tile)

    def find_on_board(self, _position):
        if self.tiles_dict.get(Vector(_position.x, _position.y, _position.z)):
            return f"Tile on position {_position} exists"
        else:
            return f"Tile on position {_position} does not exists"

    def is_available(self, tile: Tile):
        pos = tile.position  # current tile position
        #jesli nie istnieje dana pozycja
        if pos not in self.tiles_dict:
            print(f"{tile} does not exist")
            return False
        #jesli nad obecnym kafelkiem istnieje kafelek to od razu False
        if pos.above() in self.tiles_dict:
            return False

        #sprawdzenie ilosci wolnych scian (przynajmniej dwie musza byc wolne)
        free_sides = 0
        if pos.left() not in self.tiles_dict:
            free_sides += 1
        if pos.right() not in self.tiles_dict:
            free_sides += 1
        if pos.up() not in self.tiles_dict:
            free_sides += 1
        if pos.down() not in self.tiles_dict:
            free_sides += 1

        return free_sides >= 2

    def take_off_board(self, tile: Tile):
        pos = tile.position

        self.tiles_list = [t for t in self.tiles_list if t.position != pos]
        self.tiles_dict.pop(pos,None)

    def get_available_tiles(self):
        return [tile for tile in self.tiles_list if self.is_available(tile)]

    def get_board_size(self):
        max_x= max([key.x for key in self.tiles_dict.keys()])
        max_y= max([key.y for key in self.tiles_dict.keys()])

        tile_size_x, tile_size_y=60,80

        board_width = (max_x+1)*tile_size_x
        board_height = (max_y+1)*tile_size_y

        return board_width,board_height

    def shuffle_tiles(self):
        attributes = [(tile.color, tile.figure) for tile in self.tiles_list]
        random.shuffle(attributes)

        for tile, (color, figure) in zip(self.tiles_list, attributes):
            tile.color = color
            tile.figure = figure




#board = Board("Kopiec")

#print(board.find_on_board(Vector(1, 30, 2)))
#test czy usuwanie dziala
#test1=board.tiles_dict[Vector(0,0,0)]
#test2=board.tiles_dict[Vector(1,0,0)]
'''print(board.is_available(test1))
print(board.is_available(test2))
board.take_off_board(test1)
print(board.is_available(test1))
print(board.is_available(test2))'''

#print(f"Test1:\n{test1}")
#print(f"Test2:\n{test2}")
#board.shuffle_tiles()
#print(f"Test1:\n{test1}")
#print(f"Test2:\n{test2}")