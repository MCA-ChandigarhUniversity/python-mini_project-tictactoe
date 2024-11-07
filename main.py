import tkinter as tk
from models.TicTacToeModel import TicTacToeModel
from views.TicTacToeView import TicTacToeView
from controllers.TicTacToeController import TicTacToeController


def start_game():
    player_one = tk.Tk()
    player_two = tk.Tk()

    # Initialize model
    model = TicTacToeModel()

    # Initialize views without the controllers
    view1 = TicTacToeView(player_one, "Player X")
    view2 = TicTacToeView(palyer_two, "Player O")

    # Update callback functions for each player
    def update_from_player1(board, turn):
        controller2.update_view(board, turn)

    def update_from_player2(board, turn):
        controller1.update_view(board, turn)

    # Initialize controllers with the model and views
    controller1 = TicTacToeController(model, view1, is_player1=True, update_callback=update_from_player1)
    controller2 = TicTacToeController(model, view2, is_player1=False, update_callback=update_from_player2)

    # Pass the controllers to the views
    view1.set_controller(controller1)
    view2.set_controller(controller2)

    root1.mainloop()
    root2.mainloop()


if __name__ == "__main__":
    start_game()




start_game()