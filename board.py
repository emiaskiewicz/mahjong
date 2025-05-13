from tile import *
import random
import json
import pandas
import string


class Board:
    sets_data=None
    tiles=[]

    def __init__(self,set_name):
        '''self.tiles = []
        df = pandas.read_json(f"game_sets/uklady.json", orient='values')
        for pos in df['positions']:
            self.tiles.append(Tile(color=random.choice(colors),
             figure=random.choice(figures),
             position=Vector(pos[0],pos[1],pos[2])))'''
        with open(f"game_sets\\uklady.json",mode="r",encoding="utf-8") as file:
            self.sets_data=json.load(file)

        for set in self.sets_data["sets"]:
            if set["name"]==set_name:
                for pos in set["positions"]:
                    self.tiles.append(Tile(color=random.choice(colors),
                                           figure=random.choice(figures),
                                           position=Vector(pos[0], pos[1], pos[2]),
                                           points=0))

    def find_on_board(self,_position):
        for tile in self.tiles:
            if tile.position == _position:
                return f"Tile on position {_position} exists"
        return f"Tile on position {_position} does not exists"


board = Board("Kopiec")

print(board.find_on_board(Vector(1,4,2)))