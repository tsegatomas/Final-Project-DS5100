# Monte Carlo Simulator

## Metadata

- **Project Name**: Monte Carlo Simulator
- **Author**: Tomas Tsega

## Synopsis

Monte Carlo Simulator that simulates rolling dice, playing games with those dice, and analyzing the results using statistical methods. Below is an example of how to install, import, and use the module to create a die, play a game, and analyze the outcomes.

### Installation

To install the Monte Carlo Simulator module, use pip:

```sh
pip install montecarlo
```

### Usage

1. **Create Dice**

   ```python
   import numpy as np
   from montecarlo import Die

   faces = np.array([1, 2, 3, 4, 5, 6])
   die = Die(faces)
   die.change_weight(6, 5.0)  
   ```

2. **Play a Game**

   ```python
   from montecarlo import Game

   die1 = Die(faces)
   die2 = Die(faces)
   game = Game([die1, die2])
   game.play(1000) 
   results = game.show()
   print(results)
   ```

3. **Analyze a Game**

   ```python
   from montecarlo import Analyzer

   analyzer = Analyzer(game)
   jackpots = analyzer.jackpot()  
   print(f"Number of jackpots: {jackpots}")
   face_counts = analyzer.face_counts_per_roll()
   print(face_counts)
   ```

## API Description

### Die Class

- **`__init__(faces)`**: Initializes the die with faces.

  - **Parameters**: `faces` (np.array) - A NumPy array of unique faces.
  - **Raises**: `TypeError` if not a NumPy array, `ValueError` if faces are not unique.

- **`change_weight(face, new_weight)`**: Changes the weight of a specific face.

  - **Parameters**:
    - `face` - The face value to change.
    - `new_weight` (float) - The new weight for that face.
  - **Raises**: `IndexError` if face is invalid, `TypeError` if weight is not numeric.

- **`roll(num_rolls=1)`**: Rolls the die a specified number of times.

  - **Parameters**: `num_rolls` (int) - Number of times to roll the die.
  - **Returns**: A list of outcomes.

- **`show()`**: Shows the current state of the die.

  - **Returns**: A DataFrame with faces and their weights.

### Game Class

- **`__init__(dice)`**: Initializes the game with a list of similar dice.

  - **Parameters**: `dice` (list) - A list of Die objects.

- **`play(num_rolls)`**: Plays the game by rolling all dice a specified number of times.

  - **Parameters**: `num_rolls` (int) - Number of times to roll the dice.

- **`show(form='wide')`**: Shows the results of the game.

  - **Parameters**: `form` (str) - Format of the results, either 'wide' or 'narrow'.
  - **Returns**: A DataFrame of the results.
  - **Raises**: `ValueError` if form is invalid.

### Analyzer Class

- **`__init__(game)`**: Initializes the analyzer with a game object.

  - **Parameters**: `game` (Game) - The game to analyze.
  - **Raises**: `ValueError` if not a Game object.

- **`jackpot()`**: Computes the number of jackpots (all faces the same).

  - **Returns**: An integer representing the number of jackpots.

- **`face_counts_per_roll()`**: Computes the count of each face per roll.

  - **Returns**: A DataFrame of face counts.

- **`combo_count()`**: Computes the distinct combinations of faces rolled.

  - **Returns**: A DataFrame with combinations and their counts.

- **`permutation_count()`**: Computes distinct permutations of faces rolled.

  - **Returns**: A DataFrame with permutations and their counts.

