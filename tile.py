
colors = ['red','blue','green','yellow']
numbers = [1,2,3,4,5,6,7,8,9]
figures = ['dot 1','dot 2','dot 3','dot 4','dot 5','dot 6','dot 7','dot 8','dot 9',
           'bamboo 1','bamboo 2','bamboo 3','bamboo 4','bamboo 5','bamboo 6','bamboo 7','bamboo 8','bamboo 9',
           'character 1','character 2','character 3','character 4','character 5','character 6','character 7','character 8','character 9',
           'wind east','wind south','wind west','wind north',
           'dragon red','dragon green','dragon white',
           'spring','summer','autumn','winter']

class Tile:
    def __init__(self, color, number, figure, position):
        self.color = color
        self.number = number
        self.figure = figure
        self.position = position #to jest vector pozycji

    def __str__(self):
        return f"{self.color}, {self.number}, {self.figure}\n{self.position}"



class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"x={self.x} y={self.y} z={self.z}"