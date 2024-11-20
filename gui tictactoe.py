import tkinter as tk
from tkinter import messagebox

# Function to check for a winner
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical wins
        [0, 4, 8], [2, 4, 6]              # Diagonal wins
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the game is a draw
def check_draw(board):
    return all([space != " " for space in board])

# Function to handle a player's move
def player_move(board, button, player):
    index = int(button['text']) - 1
    if board[index] == " ":
        board[index] = player
        button.config(text=player)
        
        if check_winner(board, player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game(board, buttons)
        elif check_draw(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game(board, buttons)
        else:
            next_player = "O" if player == "X" else "X"
            turn_label.config(text=f"Player {next_player}'s turn")

# Function to reset the game
def reset_game(board, buttons):
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=str(i + 1))  # Reset button text
    turn_label.config(text="Player X's turn")

# Create the main window for the game
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize board
board = [" "] * 9
buttons = []

# Create buttons for the Tic-Tac-Toe grid
for i in range(9):
    button = tk.Button(root, text=str(i + 1), width=10, height=3, font=("Arial", 20),
                       command=lambda i=i: player_move(board, buttons[i], "X" if turn_label.cget("text").endswith("X's turn") else "O"))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Label to show whose turn it is
turn_label = tk.Label(root, text="Player X's turn", font=("Arial", 16))
turn_label.grid(row=3, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()
