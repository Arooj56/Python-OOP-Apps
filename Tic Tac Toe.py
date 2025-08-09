import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[' ' for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="",width=11, height=7,
                                        command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif sum(row.count(' ') for row in self.board) == 0:
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_game()
            else:
                if self.current_player == 'X':
                    self.current_player = 'O'
                else:
                    self.current_player = 'X'
        else:
            messagebox.showerror("Error", "This cell is already occupied!")

    def check_winner(self):
        for i in range(3):
            #check row
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.highlight_buttons([(i, 0), (i, 1), (i, 2)])
                return True
            #check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.highlight_buttons([(0, i), (1, i), (2, i)])
                return True
        #check diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.highlight_buttons([(0, 0), (1, 1), (2, 2)])
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.highlight_buttons([(0, 2), (1, 1), (2, 0)])
            return True

        return False

    def highlight_buttons(self, positions):
        for pos in positions:
            row, col = pos
            self.buttons[row][col].config(bg='green')

    def reset_game(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", bg='SystemButtonFace')

window = tk.Tk()
game = TicTacToe(window)
window.mainloop()

