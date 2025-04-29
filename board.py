from tile import *
import random
import json
import pandas


class Board:
    def __init__(self):
        self.tiles = []
        df = pandas.read_json(f"game_sets/uklady.json", orient='values')
        for pos in df['positions']:
            self.tiles.append(Tile(color=random.choice(colors),
             figure=random.choice(figures),
             position=Vector(pos[0],pos[1],pos[2])))

    def find_on_board(self,_position):
        for tile in self.tiles:
            if tile.position == _position:
                return f"Tile on position {_position} exists"
        return f"Tile on position {_position} does not exists"
