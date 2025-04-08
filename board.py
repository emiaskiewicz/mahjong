from tile import *
import random
import json
import pandas

with open('C:\\Users\\emilk\\OneDrive\\Pulpit\\uklady.json') as json_file:
    file_contents=json_file.read()
parsed_json=json.loads(file_contents)

class Board:
    def __init__(self):
        self.tiles = []
        for z in range(3):
            for y in range(5):
                for x in range(5):
                    self.tiles.append(Tile(color=random.choice(colors),
                     number=random.choice(numbers),
                     figure=random.choice(figures),
                     position=Vector(x,y,z)))

    def find_on_board(self,_position):
        for tile in self.tiles:
            if tile.position == _position:
                return f"Tile on position {_position} exists"
        return f"Tile on position {_position} does not exists"