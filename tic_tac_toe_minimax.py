"""
Created on Tues Aug 12 01:07:31 2023

@author:  © SkDevilS
"""
import tkinter as tk
from tkinter import messagebox

class TicTacToebySkDevilS:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe by SkDevilS")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.player_turn = True
        self.game_over = False

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('normal', 24), width=5, height=2,
                                              command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def print_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = self.board[i][j]

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(all(cell != '-' for cell in row) for row in self.board)

    def minimax(self, depth, is_maximizing):
        if self.check_winner('X'):
            return 1
        if self.check_winner('O'):
            return -1
        if self.is_board_full():
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '-':
                        self.board[i][j] = 'X'
                        eval = self.minimax(depth + 1, False)
                        self.board[i][j] = '-'
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '-':
                        self.board[i][j] = 'O'
                        eval = self.minimax(depth + 1, True)
                        self.board[i][j] = '-'
                        min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_move = (-1, -1)
        best_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    self.board[i][j] = 'X'
                    eval = self.minimax(0, False)
                    self.board[i][j] = '-'
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (i, j)
        return best_move

    def make_move(self, row, col):
        if not self.game_over and self.board[row][col] == '-':
            if self.player_turn:
                self.board[row][col] = 'X'
            else:
                self.board[row][col] = 'O'

            self.player_turn = not self.player_turn
            self.print_board()

            if self.check_winner('X'):
                self.game_over = True
                messagebox.showinfo("Game Over", "YOU won the Match!")
            elif self.check_winner('O'):
                self.game_over = True
                messagebox.showinfo("Game Over", "SYSTEM won the Match")
            elif self.is_board_full():
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
            elif not self.player_turn:
                best_move = self.find_best_move()
                self.make_move(best_move[0], best_move[1])

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TicTacToebySkDevilS()
    app.start()
