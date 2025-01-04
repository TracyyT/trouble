# Trouble Game

This is a Python-based implementation of the classic board game **Trouble**. The game allows 2-4 players to compete, aiming to get all their tokens "home" while navigating obstacles and sending opponents' tokens back to their yard.

## Features
- Playable by 2-4 players.
- Automatic dice rolling.
- Color-coded tokens for easy tracking.
- Handles game mechanics such as token movement, capturing, and turn-based play.
- Instructions displayed in-game for player guidance.
- Saves winners' names to a file.

## How to Play
1. Run the script `boardgame.py`.
2. Enter the number of players (2-4).
3. Follow the on-screen instructions:
   - Roll the dice to determine the starting player.
   - Players take turns rolling the dice and moving their tokens.
   - A token can only leave the yard with a dice roll of 6.
   - Landing on an opponent's token sends their token back to their yard.
   - The first player to get all their tokens "home" wins.

## Rules
- Players must roll the exact number to move a token into the "home" area.
- Tokens of the same color cannot occupy the same space.
- Rolling a 6 grants an extra turn.

## Setup
- Ensure you have Python installed (version 3.x recommended).
- Save the `boardgame.py` file in a directory of your choice.
- Run the script using the command:
  ```bash
  python boardgame.py
  ```

## Code Overview
- **Dice Rolls:** The `dice()` function generates a random number between 1 and 6, simulating a dice roll.
- **Game Board:** The game board is displayed using a 2D list, dynamically updated to reflect token movements.
- **Token Movement:** Functions like `moving_red`, `moving_blue`, etc., handle the movement of tokens for each player.
- **Winner Tracking:** Winners' names are saved to `winner_list.txt`.
