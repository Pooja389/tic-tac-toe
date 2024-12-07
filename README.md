# tic-tac-toe
This is a simple Python implementation of the classic **Tic Tac Toe** game for two players. The game is played on a 3x3 grid, and players take turns placing their mark (X or O) in an empty spot.
## How to Play

1. The game starts with player X.
2. Players take turns choosing a spot on the board by entering a number between 0 and 8, representing the position:
    ```
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    ```
3. If a player selects an already occupied spot, they are prompted to choose a different position.
4. The game announces the winner when one player successfully aligns three marks. If no spots are left and there is no winner, the game declares a tie.

## Features

- Displays the board after each move.
- Validates user input to ensure it is within the allowed range (0–8) and the spot is not already taken.
- Determines if a player has won or if the game is a tie.

## How to Run

1. Make sure you have Python installed on your system.
2. Copy the code into a file named `tic_tac.py`.
3. Run the program using the following command:
   ```bash
   python tic_tac.py
