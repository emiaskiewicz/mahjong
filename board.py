from tile import *
import random
import os
import json

game_sets_path = os.path.join("game_sets", "sets.json")

class Board:
    def __init__(self,_set_name):
        self.set_name=_set_name
        self.sets_data = None
        self.tiles_dict: dict[Vector, Tile] = {}  # dostep do kafelkow po pozycji - wyszukiwanie O(1)
        self.tiles_list: list[Tile] =[]
        self.load_board()

    def load_board(self):
        self.tiles_dict.clear()
        self.tiles_list.clear()
        with open(game_sets_path, mode="r", encoding="utf-8") as file:
            self.sets_data = json.load(file)

        for set in self.sets_data["sets"]:
            if set["name"] == self.set_name:
                #while len(self.get_available_tiles())==0:
                for pos in set["positions"]:
                    position = Vector(pos[0], pos[1], pos[2])
                    tile = Tile(
                        color=get_random_color(),
                        figure=get_random_figure(),
                        position=position
                    )
                    generate_tile_image(tile)
                    self.tiles_dict[position] = tile
                    self.tiles_list.append(tile)

    def reset_board(self):
        self.tiles_dict.clear()
        self.tiles_list.clear()

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
        num_tiles = self.num_of_tiles()
        for figure,val in num_tiles.items():
            if val==1:
                self.tiles_dict = {key: value for key, value in self.tiles_dict.items() if value.figure!=figure}
                self.tiles_list = [tl for tl in self.tiles_list if tl.figure != figure]

    def get_available_tiles(self):
        return [tile for tile in self.tiles_list if self.is_available(tile)]

    def get_board_size(self):
        if len(self.tiles_list)==0:
            return [0,0]
        max_x= max([key.x for key in self.tiles_dict.keys()])
        max_y= max([key.y for key in self.tiles_dict.keys()])

        tile_size_x, tile_size_y=60,80

        board_width = (max_x+1)*tile_size_x
        board_height = (max_y+1)*tile_size_y

        return board_width,board_height

    def num_of_tiles(self):
        num_tiles={}
        for tile in self.tiles_list:
            if tile.figure not in num_tiles:
                num_tiles[tile.figure] = 0
            num_tiles[tile.figure]+=1
        return num_tiles

    def shuffle_tiles(self):
        attributes = [(tile.color, tile.figure) for tile in self.tiles_list]
        random.shuffle(attributes)

        for tile, (color, figure) in zip(self.tiles_list, attributes):
            tile.color = color
            tile.figure = figure