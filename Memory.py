import random

def create_board(rows, cols):
    symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    num_pairs = (rows * cols) // 2
    pairs = random.sample(symbols, num_pairs) * 2
    random.shuffle(pairs)
    board = [[None] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            board[i][j] = pairs.pop()
    return board

def display_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=" ")
            else:
                print("X", end=" ")
        print()

def main():
    rows = 4
    cols = 4
    board = create_board(rows, cols)
    revealed = [[False] * cols for _ in range(rows)]
    
    pairs_found = 0
    attempts = 0
    
    while pairs_found < (rows * cols) // 2:
        display_board(board, revealed)
        
        row1 = int(input("Enter the row of the first card: "))
        col1 = int(input("Enter the column of the first card: "))
        
        row2 = int(input("Enter the row of the second card: "))
        col2 = int(input("Enter the column of the second card: "))
        
        if (0 <= row1 < rows and 0 <= col1 < cols) and \
           (0 <= row2 < rows and 0 <= col2 < cols) and \
           not revealed[row1][col1] and not revealed[row2][col2]:
            
            if board[row1][col1] == board[row2][col2]:
                print("You found a pair!")
                revealed[row1][col1] = True
                revealed[row2][col2] = True
                pairs_found += 1
            else:
                print("Try again!")
                
            attempts += 1
        else:
            print("Invalid input. Try again.")
        
    print("Congratulations! You completed the game in", attempts, "attempts.")

if __name__ == "__main__":
    main()
