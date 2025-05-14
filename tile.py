from PIL import Image

colors = ['red','blue','green','yellow']
figures = ['dot 1','dot 2','dot 3','dot 4','dot 5','dot 6','dot 7','dot 8','dot 9',
           'bamboo 1','bamboo 2','bamboo 3','bamboo 4','bamboo 5','bamboo 6','bamboo 7','bamboo 8','bamboo 9',
           'character 1','character 2','character 3','character 4','character 5','character 6','character 7','character 8','character 9',
           'wind east','wind south','wind west','wind north',
           'dragon red','dragon green','dragon white',
           'spring','summer','autumn','winter']

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"x={self.x} y={self.y} z={self.z}"

    def above(self):
        return Vector(self.x,self.y,self.z+1)

    def left(self):
        return Vector(self.x-1,self.y,self.z)

    def right(self):
        return Vector(self.x+1,self.y,self.z)

    def up(self):
        return Vector(self.x,self.y-1,self.z)

    def down(self):
        return Vector(self.x,self.y+1,self.z)

class Tile:
    color=''
    figure=''
    position=Vector(0,0,0)
    points = 0

    def __init__(self, color, figure, position, points):
        self.color = color
        self.figure = figure
        self.position = position #to jest vector pozycji
        self.points = points

    def __str__(self):
        return f"{self.color}, {self.figure}\n{self.position}"

    def __eq__(self, other):
        #to jest tylko dla identycznych jesli chce wprowadzic punktacje trzeba to zmienic
        return self.position==other.position and self.color==other.color and self.figure == other.figure

    def display(self): #wyswietlenie kafelka w grze
        pass



#funkcja do generowania wygladu kafelka
def generate_tile_image(tile):

    color_img = Image.open(f"assets_images/colors/{tile.color}.png").convert("RGBA")
    figure_img = Image.open(f"assets_images/figures/{tile.figure}.png").convert("RGBA")

    x = 341 - figure_img.width // 2 - 36
    y = 438 - figure_img.height // 2 - 28
    color_img.paste(figure_img, (x, y), figure_img)

    out_path = "generated_tiles/" + tile.color + "_" + tile.figure + ".png"
    color_img.save(out_path)