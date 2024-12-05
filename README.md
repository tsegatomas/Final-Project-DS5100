# Monte Carlo Simulator

## Metadata
**Project Name**: Monte Carlo Simulator
**Author**: Tomas Tsega

## Synopsis
The Monte Carlo Simulator allows users to simulate games involving dice and analyze the results. The main classes are `Die`, `Game`, and `Analyzer`. 

### Installation
To install the Monte Carlo Simulator use the following command:
```sh
pip install .
```

### Usage

#### Importing the Package
```python
from montecarlo_simulator import Die, Game, Analyzer
```

#### Creating Dice
```python
import numpy as np

faces = np.array([1, 2, 3, 4, 5, 6])
die = Die(faces)
```

#### Changing Weights of a Die
```python
die.change_weight(6, 5.0)  # Changing the weight of face '6' to 5.0
```

#### Playing a Game
```python
game = Game([die])
game.play(rolls=1000)  # Rolling the die 1000 times
```

#### Analyzing the Game
```python
analyzer = Analyzer(game)
print(analyzer.jackpot())  # Count the number of jackpots
print(analyzer.face_counts_per_roll())  # Count of each face per roll
```

## API Description

### Die Class
- **`Die(faces: np.ndarray)`**
  - **Description**: Initializes a die with given faces.
  - **Parameters**:
    - `faces` (np.ndarray): An array of distinct values representing the die faces.
  - **Raises**: `TypeError` if the input is not a NumPy array, `ValueError` if the values are not distinct.
  - **Attributes**: Initializes a private DataFrame storing faces and weights.

- **`change_weight(face, new_weight)`**
  - **Description**: Changes the weight of a given face.
  - **Parameters**:
    - `face`: The face whose weight needs to be changed.
    - `new_weight` (float): The new weight for the face.
  - **Raises**: `IndexError` if the face does not exist, `TypeError` if the weight is not numeric.

- **`roll(rolls=1)`**
  - **Description**: Rolls the die a given number of times.
  - **Parameters**: `rolls` (int): The number of times to roll the die.
  - **Returns**: A list of outcomes.

- **`show()`**
  - **Description**: Returns the current state of the die.
  - **Returns**: A DataFrame containing faces and their corresponding weights.

### Game Class
- **`Game(dice: list)`**
  - **Description**: Initializes the game with a list of dice.
  - **Parameters**:
    - `dice` (list): List of `Die` objects.
  - **Raises**: `TypeError` if the list does not contain valid `Die` objects.

- **`play(rolls=1)`**
  - **Description**: Rolls all dice a given number of times.
  - **Parameters**: `rolls` (int): The number of times to roll the dice.
  - **Stores**: The results of the rolls in a private DataFrame.

- **`show(form='wide')`**
  - **Description**: Shows the results of the most recent play.
  - **Parameters**: `form` (str): `'wide'` or `'narrow'`. Defaults to `'wide'`.
  - **Returns**: A DataFrame in the specified format.
  - **Raises**: `ValueError` if an invalid form is provided.

### Analyzer Class
- **`Analyzer(game: Game)`**
  - **Description**: Initializes the analyzer with a game object.
  - **Parameters**: `game` (Game): A `Game` object to be analyzed.
  - **Raises**: `TypeError` if the input is not a `Game` object.

- **`jackpot()`**
  - **Description**: Computes the number of times all dice rolled the same face.
  - **Returns**: An integer representing the number of jackpots.

- **`face_counts_per_roll()`**
  - **Description**: Computes the counts of each face per roll.
  - **Returns**: A DataFrame with face counts per roll.

- **`combo_count()`**
  - **Description**: Computes distinct combinations of faces rolled.
  - **Returns**: A DataFrame with combinations and their counts.

- **`permutation_count()`**
  - **Description**: Computes distinct permutations of faces rolled.
  - **Returns**: A DataFrame with permutations and their counts.

- **`scrabble_word_analysis(word_list)`**
  - **Description**: Checks if rolls form valid Scrabble words.
  - **Parameters**: `word_list` (list): A list of valid Scrabble words.
  - **Returns**: A DataFrame indicating which rolls form valid words.

- **`letter_frequency_analysis(letter_frequencies)`**
  - **Description**: Computes the frequency of each letter rolled compared to expected frequencies.
  - **Parameters**: `letter_frequencies` (dict): Expected frequencies of letters.
  - **Returns**: A DataFrame comparing rolled counts to expected frequencies.


