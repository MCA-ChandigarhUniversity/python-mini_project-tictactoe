import tkinter as tk
from tkinter import messagebox

class TicTacToeView:
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.controller = None
        self.buttons = []

        # Create a 3x3 grid of buttons
        for i in range(9):
            button = tk.Button(master, text="", font="Arial 20", width=5, height=2,
                               command=lambda i=i: self.controller.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Turning indicator
        self.turn_label = tk.Label(master, text="Player X turns", font="Arial 14")
        self.turn_label.grid(row=3, column=0, columnspan=3)

        # Binding Ctrl+R to restart the game
        master.bind("<Control-r>", lambda e: self.controller.reset_game())

    def set_controller(self, controller):
        self.controller = controller

    def update_board(self, board, turn):
        for i, value in enumerate(board):
            self.buttons[i].config(text=value, state="disabled" if value else "normal")
        self.turn_label.config(text="Your Turn" if turn == self.controller.get_player_symbol() else "Opponent's Turn")

    def show_winner(self, winner, winning_cells):
        if winner == "Draw":
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        else:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")

