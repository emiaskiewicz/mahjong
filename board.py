from tile import *
import random
import json
import pandas
import string


class Board:
    sets_data = None
    tiles_dict: dict[Vector, Tile] = {}  # dostep do kafelkow po pozycji - wyszukiwanie O(1)
    tiles_list = []

    def __init__(self, set_name):
        with open(f"game_sets\\uklady.json", mode="r", encoding="utf-8") as file:
            self.sets_data = json.load(file)

        for set in self.sets_data["sets"]:
            if set["name"] == set_name:
                for pos in set["positions"]:
                    position = Vector(pos[0], pos[1], pos[2])
                    tile = Tile(
                        color=random.choice(colors),
                        figure=random.choice(figures),
                        position=position,
                        points=0
                    )
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

    def shuffle_tiles(self):
        attributes = [(tile.color, tile.figure) for tile in self.tiles_list]
        random.shuffle(attributes)

        for tile, (color, figure) in zip(self.tiles_list, attributes):
            tile.color = color
            tile.figure = figure




board = Board("Kopiec")

#print(board.find_on_board(Vector(1, 30, 2)))
#testtile=Tile('red','dot 7',Vector(0,0,0),0)

#print(board.is_available(testtile))
