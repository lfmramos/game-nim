# NIM Game Implementation

## Overview
This is a Python implementation of the mathematical strategy game NIM, where players take turns removing objects from distinct heaps. In this version, the game is played against a computer that implements the optimal winning strategy.

## Game Rules
1. The game starts with a pile of `n` pieces
2. Players take turns removing pieces from the pile
3. On each turn, a player must remove at least 1 piece and at most `m` pieces
4. The player who removes the last piece wins
5. The computer uses an optimal strategy based on the (m+1) rule

## Features
- Single game mode
- Championship mode (best of 3)
- Computer player with optimal strategy
- Input validation
- Interactive gameplay

## Game Modes
1. **Single Game**: Play one isolated game against the computer
2. **Championship**: Play a series of three games against the computer

## Functions

### Core Game Logic
- `computador_escolhe_jogada(n, m)`: Implements the computer's optimal strategy
- `usuario_escolhe_jogada(n, m)`: Handles player moves with input validation
- `partida()`: Manages a single game
- `campeonato()`: Handles a championship (3 games)
- `main()`: Game initialization and mode selection

### Strategic Implementation
The computer uses the optimal winning strategy based on the (m+1) rule:
- Tries to leave a multiple of (m+1) pieces after its move
- If no optimal move is found, removes m pieces

## How to Play
1. Run the program
2. Choose game mode:
   - Enter 1 for a single game
   - Enter 2 for championship mode
3. Input the initial number of pieces (n)
4. Input the maximum pieces that can be removed per turn (m)
5. Follow the prompts to make your moves

Example:
```python
python nim_game.py
```

## Game Flow
1. Program determines who starts based on optimal strategy
2. Players alternate turns
3. On each turn:
   - Current game state is displayed
   - Player selects number of pieces to remove
   - Move validity is checked
4. Game ends when no pieces remain

## Input Validation
The program validates:
- Game mode selection (1 or 2)
- Number of pieces to remove (between 1 and m)
- Available pieces (can't remove more than remaining)

## Technical Notes
- Written in Python 3.x
- No external dependencies required
- Implements optimal NIM game strategy
- Includes input validation and error handling

## Mathematical Strategy
The computer's strategy is based on the mathematical principle that:
- If n is a multiple of (m+1), the next player to move will lose with optimal play
- Otherwise, there exists a move that leaves a multiple of (m+1) pieces, leading to a win

## Contributing
Feel free to submit issues and enhancement requests. Areas for potential improvement:
- Graphical user interface
- Additional game modes
- Statistics tracking
- Difficulty levels
