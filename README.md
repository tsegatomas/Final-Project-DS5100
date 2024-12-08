# Monte Carlo Simulator Project

## Metadata
- **Author:** Tomas
- **Repository URL:** [https://github.com/tsegatomas/Final-Project-DS5100.git](https://github.com/tsegatomas/Final-Project-DS5100.git)
- **Version:** 1.0.0
- **License:** MIT License

## Synopsis
This project implements a Monte Carlo simulation framework for working with dice, games, and analyzing their outcomes. It includes three main classes:

1. **Die**: Represents a die with customizable faces and weights.
2. **Game**: Simulates rolling one or more dice.
3. **Analyzer**: Provides analytical tools for interpreting game results.

### Example Usage
```python
import numpy as np
from montecarlo_simulator.montecarlo import Die, Game, Analyzer

# Create a die with faces A, B, C
faces = np.array(['A', 'B', 'C'])
die = Die(faces)
die.change_weight('A', 5)

# Create a game with two dice
game = Game([die, die])
game.play(10)
results = game.show()

# Analyze the game
analyzer = Analyzer(game)
jackpot_count = analyzer.jackpot()
face_counts = analyzer.face_counts_per_roll()
```

## API

### Die Class
**Constructor**:
```python
Die(faces: np.ndarray)
```
- Initializes a die with the given faces.

**Methods**:
- `change_weight(face, new_weight)`: Changes the weight of a specific face.
- `roll(rolls=1)`: Rolls the die a specified number of times.
- `show()`: Returns a DataFrame showing faces and their weights.

### Game Class
**Constructor**:
```python
Game(dice: list[Die])
```
- Initializes a game with a list of `Die` objects.

**Methods**:
- `play(rolls=1)`: Plays the game by rolling the dice a specified number of times.
- `show(form='wide')`: Returns the results in 'wide' or 'narrow' format.

### Analyzer Class
**Constructor**:
```python
Analyzer(game: Game)
```
- Initializes the analyzer with a `Game` object.

**Methods**:
- `jackpot()`: Counts the number of jackpots (all faces the same in a roll).
- `face_counts_per_roll()`: Computes the frequency of each face per roll.
- `combo_count()`: Counts unique combinations of faces, order-independent.
- `permutation_count()`: Counts unique permutations of faces, order-dependent.

---

For more details, visit the [repository](https://github.com/tsegatomas/Final-Project-DS5100.git).


