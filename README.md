# Woven Monopoly

A command-line application using Python that simulates deterministic games of Woven Monopoly using predefined dice rolls.

## Requirements

- Python 3.x
- pytest

## Setup

Install pytest:

```bash
pip install pytest
```

## Run

```bash
python main.py rolls_1.json
python main.py rolls_2.json
```

## Test

```bash
python -m pytest tests/
```

## Results

**Game 1 (rolls_1.json)**
- Charlotte goes bankrupt
- Winner: Peter with $40

**Game 2 (rolls_2.json)**
- Sweedal goes bankrupt
- Winner: Charlotte with $31

## Design Decisions

- **Separation of concerns** - Board, Player and Game logic are split into separate classes
- **Extensibility** - new space types can be added by extending the Space class in board.py
- **Utility module** - JSON loading is handled in utils.py so it is not tied to any specific class
- **Deterministic simulation** - given the same dice rolls, the game will always produce the same result

## Project Structure

```
woven_monopoly/
├── main.py
├── board.json
├── rolls_1.json
├── rolls_2.json
├── game/
│   ├── board.py
│   ├── player.py
│   ├── game.py
│   └── utils.py
└── tests/
    ├── test_board.py
    ├── test_player.py
    └── test_game.py
```
