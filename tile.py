import random
from PIL import Image
import os

from display import draw_board

#wszystkie mozliwosci cech kafelkow
colors = {'red': 0.1, 'blue': 0.2, 'green': 0.3, 'yellow': 0.4}
dot_fig =['dot 1','dot 2','dot 3','dot 4','dot 5','dot 6','dot 7','dot 8','dot 9']
bambooo_fig = ['bamboo 1','bamboo 2','bamboo 3','bamboo 4','bamboo 5','bamboo 6','bamboo 7','bamboo 8','bamboo 9']
character_fig = ['character 1','character 2','character 3','character 4','character 5','character 6','character 7','character 8','character 9']
wind_fig =['wind east','wind south','wind west','wind north']
dragon_fig=['dragon red','dragon green','dragon white']


#klasa Vector - sluzy do przechowywania wspolrzednych kafelka
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return (self.x,self.y,self.z)== (other.x,other.y,other.z)

    def __str__(self):
        return f"x={self.x} y={self.y} z={self.z}"

    def __hash__(self):
        return hash((self.x,self.y,self.z))

    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"

    #metody do sprawdzenia czy w ich otoczeniu sa inne kafelki
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

#klasa Tile - przechowuje wszystkie informacje o danych kafelkach
class Tile:
    color=''
    figure=''
    position=Vector(0,0,0)
    points = 3

    def __init__(self, color, figure, position: Vector):
        self.color = color
        self.figure = figure
        self.position = position #to jest vector pozycji
        self.set_points() #inicjalizacja punktacji kafelka na podstawie jego cech

    def __str__(self):
        return f"{self.color}, {self.figure},\tposition: {self.position}, points: {self.points}"

    def __eq__(self, other):
        return self.position==other.position and self.color==other.color and self.figure == other.figure

    #metoda set_points, ktora na podstawie cech kafelka przypisuje im ilosc punktow,
    #kafelek od razu ma przypisana wartosc punktowa 3 a dane figury moga ja zwiekszyc
    def set_points(self):
        figure= self.figure.split(" ")

        match figure[0]:
            case "dot" | "bamboo" | "character":
                self.points += 5
            case "wind":
                self.points+=7
            case "dragon":
                self.points+=10

    #metoda do pobrania nazwy kafelka na podstawie jego cech,
    #ta sama nazwa jest wykorzystywana przy nazewnictwie plikow z grafikami kafelkow
    def get_tile_name(self):
        return self.color + "_" + self.figure

#funkcja generuje liste figur z ktorych beda wybierane do planszy,
#sa z rozna iloscia - dot, bamboo i character beda losowane czesciej od
#wind i dragon
def generate_figures_list():
    all_fig =[]
    all_fig+=dot_fig*6
    all_fig+=bambooo_fig*6
    all_fig+=character_fig*6
    all_fig+=wind_fig*2
    all_fig+=dragon_fig*2
    return all_fig

def get_random_figure():
    figures=generate_figures_list()
    return random.choice(figures)

def get_random_color():
    colors_list = list(colors.keys())
    weights_list = list(colors.values())
    return random.choices(colors_list,weights=weights_list,k=1)[0]

#funkcja do generowania wygladu kafelka,
#pobiera czesciowe grafiki danych cech i sklada je w jedna grafike kafelka
def generate_tile_image(tile):
    colors_image_path = os.path.join("assets_images","colors",tile.color)+".png"
    figures_image_path = os.path.join("assets_images","figures",tile.figure)+".png"
    color_img = Image.open(colors_image_path).convert("RGBA")
    figure_img = Image.open(figures_image_path).convert("RGBA")

    x = 341 - figure_img.width // 2 - 36
    y = 438 - figure_img.height // 2 - 28
    color_img.paste(figure_img, (x, y), figure_img)
    color_img = color_img.resize((70,90), Image.Resampling.LANCZOS)
    out_name = tile.color + "_" + tile.figure + ".png"
    out_path = os.path.join("generated_tiles",out_name)
    color_img.save(out_path)