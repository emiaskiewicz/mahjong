from itertools import combinations
from board import *
from tile import *
from display import draw_board

class Logic:
    board = Board("Kopiec")

    def __init__(self,rules):
        self.rules = rules

    def run_game_loop(self, screen):
        import pygame
        running = True
        clock = pygame.time.Clock()

        while running:
            screen.fill((30, 30, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # obsługa kliknięć itp. (opcjonalnie teraz)

            draw_board(screen, self.board)
            pygame.display.flip()
            clock.tick(60)


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

    def find_possible_moves(self, board: Board):
        #wszystkie mozliwe kombinacje ruchow (2 lub 3 kafelki do zdjecia) -> zwraca liste dostepnych ruchow
        accessible = board.get_available_tiles()
        moves = []

        for move in combinations(accessible,2):
            if self.can_remove(list(move),board):
                moves.append(list(move))

        for move in combinations(accessible,3):
            if self.can_remove(list(move),board):
                moves.append(list(move))

        return moves


    def get_hint(self, board: Board):
        moves = self.find_possible_moves(board)
        if not moves:
            return None
        return random.choice(moves)

    def solve(self):
        pass

    def game(self):
        board = Board("Kopiec")
