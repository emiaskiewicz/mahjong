import random

class Player:
    player_name='username'
    game_mode = ' '
    difficulty = ' '
    set_name = ' '
    points = 0

    def __init__(self):
        pass

    def set_player_name(self,_new_name):
        self.player_name=_new_name

    def set_game_mode(self, _new_mode, _val):
        self.game_mode = _new_mode
        print(_val)

    def set_difficulty(self,_new_diff,_val):
        self.difficulty = _new_diff
        print(_val)

    def set_gameSet(self,_new_name,_val):
        self.set_name = _new_name
        print(_val)

    def get_gameSet(self):
        return self.set_name[0][0]

    def get_gameMode(self):
        return self.game_mode[0][0]

    def print_rules(self):
        return print(f"Info\nPlayer name: {self.player_name}\tGame mode: {self.game_mode}\t"
                     f"Difficulty: {self.difficulty}\tGame set: {self.set_name}")

    def add_points(self,points):
        self.points+=points

    def reset_points(self):
        self.points=0

    def save_rules(self,dict):
        self.rules=dict
        print(self.rules)

class CPU(Player):
    chosen_tiles =[]

    def __init__(self,name,game):
        super().__init__()
        self.player_name = name
        self.game = game

    def select_move(self):
        available_moves = self.game.find_possible_moves(self.game.board)
        if not available_moves:
            return None
        scores = [(move,self.game.score(move)) for move in available_moves]
        max_score = max(score for move,score in scores)
        best_moves = [move for move, score in scores if score == max_score]

        if self.get_gameMode() == "easy":
            self.chosen_tiles = available_moves[0]
        elif self.get_gameMode() == "normal":
            if random.randint(1,10) == 10:
                self.chosen_tiles = random.choice(best_moves)
            else:
                sorted_scores = sorted(scores,key=lambda x: x[1])
                mid = len(sorted_scores)//2
                self.chosen_tiles = sorted_scores[mid][0]
        elif self.get_gameMode() =="hard":
            self.chosen_tiles = random.choice(best_moves)
        self.game.selected_tiles=self.chosen_tiles
        return self.chosen_tiles