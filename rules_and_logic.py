from itertools import combinations
from time import sleep
import pygame.font
from board import *
from tile import *
from players import CPU
from display import (draw_board,handle_click,end_game_message, draw_hint_button,
                     draw_delete_button, no_hint_message,game_win_screen, draw_back_button)


class Logic:
    selected_tiles = []
    hint_tiles = []

    def __init__(self,player):
        self.player = player
        self.board = Board(self.player.get_gameSet())

    def single_player_mode(self, screen):
        import pygame
        running = True
        clock = pygame.time.Clock()
        #opoznienie zeby plansza miala czas sie zaladowac
        pygame.time.delay(400)
        draw_board(screen, self.board, self.selected_tiles)
        pygame.display.flip()

        while running:
            screen.fill((30, 30, 30))

            hint_button_obj = draw_hint_button(screen)
            delete_button_obj = draw_delete_button(screen)
            back_button_obj = draw_back_button(screen)

            font = pygame.font.Font(None,36)
            points_text=font.render(f'Score: {self.player.points}',True,(255,255,255))
            screen.blit(points_text,(15,screen.get_height()-points_text.get_height()-15))

            if not self.any_valid_moves(self.board):
                if self.board.get_board_size() == [0, 0]:
                    menu_button, restart_button = game_win_screen(screen, self.player.points,
                                                                  self.player.player_name)
                elif self.board.get_board_size()!=[0,0] and len(self.board.tiles_list)==2:
                    print("remis")
                else:
                    quit_button, shuffle_button = end_game_message(screen)

                waiting_for_click = True
                while waiting_for_click:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            waiting_for_click = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if self.handle_win_screen_click(mouse_pos,menu_button,restart_button):
                                running = False
                                waiting_for_click = False
                            elif self.handle_end_game_click(mouse_pos, quit_button, shuffle_button, self.board):
                                running = False
                                waiting_for_click = False
                            else:
                                waiting_for_click = False
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.handle_hint_click(mouse_pos, hint_button_obj,screen):
                        draw_board(screen, self.board, self.hint_tiles)
                        pygame.display.flip()
                        sleep(3)
                    if self.handle_delete_click(mouse_pos,delete_button_obj):
                        draw_board(screen,self.board,self.selected_tiles)
                        pygame.display.flip()
                    if self.handle_back_click(mouse_pos,back_button_obj):
                        running=False

                    handle_click(screen, self.board, mouse_pos,self.selected_tiles,self)

            draw_board(screen, self.board,self.selected_tiles)
            pygame.display.flip()
            clock.tick(60)

    def cpu_vs_cpu_mode(self, screen):
        import pygame
        running = True
        clock = pygame.time.Clock()
        cpu1 = CPU("CPU 1",self)
        cpu2 = CPU("CPU 2",self)
        current_cpu = cpu1
        #opoznienie zeby plansza miala czas sie zaladowac
        pygame.time.delay(400)
        draw_board(screen, self.board, self.selected_tiles)
        pygame.display.flip()

        while running:
            screen.fill((30, 30, 30))

            back_button_obj = draw_back_button(screen)

            font = pygame.font.Font(None,36)
            points1_text=font.render(f'Score: {cpu1.points}',True,(255,255,255))
            screen.blit(points1_text,(15,screen.get_height()-points1_text.get_height()-15))
            cpu1_text = font.render(f'CPU 1', True, (255, 255, 255))
            screen.blit(cpu1_text, (15, screen.get_height() - cpu1_text.get_height() - points1_text.get_height() - 15))

            points2_text = font.render(f'Score: {cpu2.points}', True, (255, 255, 255))
            screen.blit(points2_text, (screen.get_width()-points2_text.get_width()-15,
                                       screen.get_height() - points2_text.get_height() - 15))
            cpu2_text = font.render(f'CPU 2', True, (255, 255, 255))
            screen.blit(cpu2_text, (screen.get_width() - cpu2_text.get_width() -15, screen.get_height() - cpu2_text.get_height() - points2_text.get_height() - 15))

            if not self.any_valid_moves(self.board):
                if self.board.get_board_size() == [0, 0]:
                    winner = cpu1
                    if cpu1.points<cpu2.points:
                        winner = cpu2
                    menu_button, restart_button = game_win_screen(screen, winner.points,
                                                                  winner.player_name)
                elif self.board.get_board_size()!=[0,0] and len(self.board.tiles_list)==2:
                    print("remis")
                else:
                    quit_button, shuffle_button = end_game_message(screen)

                waiting_for_click = True
                while waiting_for_click:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            waiting_for_click = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if self.handle_win_screen_click(mouse_pos,menu_button,restart_button):
                                running = False
                                waiting_for_click = False
                            elif self.handle_end_game_click(mouse_pos, quit_button, shuffle_button, self.board):
                                running = False
                                waiting_for_click = False
                            else:
                                waiting_for_click = False
                continue
            else:
                moved = self.remove_tiles_ai(current_cpu,screen)
                if moved:
                    current_cpu = cpu2 if current_cpu == cpu1 else cpu1
                    pygame.time.delay(500)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.handle_back_click(mouse_pos,back_button_obj):
                        running=False

                    handle_click(screen, self.board, mouse_pos,self.selected_tiles,self)

            draw_board(screen, self.board,self.selected_tiles)
            pygame.display.flip()
            clock.tick(60)

    def reset_game(self):
        self.player.reset_points()
        self.selected_tiles.clear()
        self.hint_tiles.clear()
        self.board.reset_board()

    def handle_end_game_click(self, pos, quit_button, shuffle_button, board):
        if quit_button.collidepoint(pos):
            from main import mainmenu
            mainmenu._open()
            return True
        elif shuffle_button.collidepoint(pos):
            board.shuffle_tiles()
            return False
        return False

    def handle_back_click(self,pos,back_button):
        if back_button.collidepoint(pos):
            self.reset_game()
            return True
        return False

    def handle_win_screen_click(self,pos, menu_button,restart_button):
        if menu_button.collidepoint(pos):
            from main import mainmenu
            mainmenu._open()
            return True
        elif restart_button.collidepoint(pos):
            self.reset_game()
            return True
        return False

    def handle_hint_click(self, pos, hint_but,screen):
        if hint_but.collidepoint(pos):
            hint = self.get_hint(self.board)
            if hint=="pts":
                no_hint_message(screen)
                pygame.display.flip()
                sleep(4)
                return True
            elif hint:
                self.hint_tiles.clear()
                for tile in hint:
                    self.hint_tiles.append(tile)
                return True
        return False

    def handle_delete_click(self, pos, delete_but):
        if delete_but.collidepoint(pos):
            if len(self.selected_tiles) in (2, 3):
                score = self.remove_matching(tiles=self.selected_tiles, board=self.board)
                if score > 0:
                    print(f"Punkty: {score}")
                    self.player.add_points(score)
                    self.selected_tiles.clear()
                    return True
                if score == 0:
                    self.selected_tiles.clear()
        return False

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
        return self.matching_features(tiles)[1]

    def score(self,tiles: list[Tile]):
        #oblicza punkty za pojedyncze zdjecie kafelkow
        common = self.matching_features(tiles)
        if not any(common):
            return 0
        points_sum = sum(tile.points for tile in tiles)

        if common[0] and common[1]:
            points_sum *= 5
        elif common[0]:
            points_sum *= 2
        elif common[1]:
            points_sum *= 3

        if tiles[0].color == 'white':
            return points_sum

        color_counts = {}
        for tile in tiles:
            if tile.color not in color_counts:
                color_counts[tile.color] = 0
            color_counts[tile.color] += 1

        for color, count in color_counts.items():
            if count >= 2:
                if color == 'red':
                    points_sum*=5
                elif color == 'blue':
                    points_sum*=4
                elif color == 'green':
                    points_sum *= 3
                elif color == 'yellow':
                    points_sum*=2
                break

        return points_sum

    def remove_matching(self,tiles: list[Tile],board: Board):
        #usuwa kafelki jesli to mozliwe, zwraca ilosc punktow za ruch
        if self.can_remove(tiles,board):
            for t in tiles:
                board.take_off_board(t)
            return self.score(tiles)
        else:
            return 0

    def remove_tiles_ai(self,cpu: CPU,screen):
        move = cpu.select_move()
        if move:
            draw_board(screen,self.board, move)
            pygame.display.flip()
            pygame.time.delay(600)
            score = self.remove_matching(move,self.board)
            if score > 0:
                print(f"Punkty: {score}")
                cpu.add_points(score)
                cpu.game.selected_tiles.clear()
                return True
            if score == 0:
                cpu.game.selected_tiles.clear()
        return False

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
        if self.player.points < 100:
            print("Not enough points for a hint")
            return "pts"
        else:
            self.player.add_points(-100)
        return random.choice(moves)

    def game_mode(self,screen):
        game_mode = self.player.get_gamemode()
        if game_mode == "Single player":
            self.single_player_mode(screen)
        elif game_mode == "CPU vs CPU":
            self.cpu_vs_cpu_mode(screen)
        elif game_mode == "Player vs CPU":
            print("human vs ai")
