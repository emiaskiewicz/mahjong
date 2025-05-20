from board import *
from tile import *

class GameLogic:
    def __init__(self):
        pass

    def matching_features(self,tiles: list[Tile]):
        #zwraca liste [ten_sam_kolor, ta_sama_figura] jako boolean
        matchList = [False, False]

        if len(tiles) < 2:
            return [False,False]
        elif len(tiles)==2:
            if tiles[0].color == tiles[1].color:
                matchList[0] = True
            if tiles[0].figure == tiles[1].figure:
                matchList[1] = True
        elif len(tiles)==3:
            if all(tile.color == tiles[0].color for tile in tiles):
                matchList[0] = True
            if all(tile.figure == tiles[0].figure for tile in tiles):
                matchList[1] = True
        return matchList

    def can_remove(self,tiles: list[Tile], board: Board):
        #sprawdza czy mozna zdjac zaznaczone kafelki
        if len(tiles) not in (2,3):
            return False
        if not all(board.is_available(tile) for tile in tiles):
            return False
        return any(self.matching_features(tiles))

    def score(self,tiles: list[Tile]):
        #oblicza punkty za pojedyncze zdjecie kafelkow
        common = self.matching_features(tiles)
        sum = 0
        if not any(common):
            return sum
        for t in tiles:
            sum+=t.points
        if common[0] and common[1]:
            sum*=5
        elif common[0]:
            sum*=2
        elif common[1]:
            sum *= 3
        return sum

    def remove_matching(self,tiles: list[Tile],board: Board):
        #usuwa kafelki jesli to mozliwe, zwraca ilosc punktow za ruch
        if self.can_remove(tiles,board):
            for t in tiles:
                board.take_off_board(t)
            return self.score(tiles)
        else:
            return 0


    def any_valid_moves(self, board: Board):
        #sprawdza czy istnieje poprawny ruch
        accessible = board.get_available_tiles()
        for i in range(len(accessible)):
            for j in range(i+1,len(accessible)):
                if self.can_remove([accessible[i],accessible[j]],board):
                    return True
        return False


    def hint(self):
        pass

    def solve(self):
        pass

    def game(self):
        board = Board("Kopiec")