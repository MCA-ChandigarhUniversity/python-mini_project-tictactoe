class TicTacToeModel:
    def __init__(self):
        self.board = [""] * 9
        self.current_turn = 'X'

    def make_move(self, index, player):
        if self.board[index] == "":
            self.board[index] = player
            self.current_turn = 'O' if player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return self.board[combo[0]], combo
        if "" not in self.board:
            return "Draw", []
        return None, []
    
    def reset(self):
        self.board = [""] * 9
        self.current_turn = 'X'
