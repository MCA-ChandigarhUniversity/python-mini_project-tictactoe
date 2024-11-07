class TicTacToeController:
    def __init__(self, model, view, is_player1, update_callback):
        self.model = model
        self.view = view
        self.is_player1 = is_player1
        self.update_callback = update_callback

    def get_player_symbol(self):
        return 'X' if self.is_player1 else 'O'

    def make_move(self, index):
        if self.model.current_turn == self.get_player_symbol():
            if self.model.make_move(index, self.get_player_symbol()):
                winner, winning_cells = self.model.check_winner()
                self.view.update_board(self.model.board, self.model.current_turn)
                if winner:
                    self.view.show_winner(winner, winning_cells)
                    self.reset_game()
                else:
                    self.update_callback(self.model.board, self.model.current_turn)

    def update_view(self, board, turn):
        self.model.board = board
        self.model.current_turn = turn
        self.view.update_board(board, turn)

    def reset_game(self):
        self.model.reset()
        self.view.reset_view()
        self.update_callback(self.model.board, self.model.current_turn)
