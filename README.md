# Monte Carlo Simulator Project

## Metadata
- **Project Name**: Monte Carlo Simulator
- **Author**: Tomas Tsega
- **Repository URL**: [GitHub Repository](https://github.com/tsegatomas/Final-Project-DS5100.git)

---

## Synopsis
This Monte Carlo Simulator allows to simulate random processes by rolling weighted dice, playing games with dice, and analyzing the outcomes using statistical methods.

### Installation
To install the project locally, clone the repository and use the following commands:
```bash
# Clone the repository
git clone git@github.com:tsegatomas/Final-Project-DS5100.git

# Navigate to the project directory
cd Final-Project-DS5100

# Install the package
pip install -e .
```

### Usage
Below are examples showing how to use the Die, Game, and Analyzer classes:

#### Create and Roll a Die
```python
from montecarlo_simulator.montecarlo import Die

# Create a die with faces 1 through 6
die = Die(np.array([1, 2, 3, 4, 5, 6]))

# Change the weight of face 1 to 3.0
die.change_weight(1, 3.0)

# Roll the die 10 times
outcomes = die.roll(10)
print(outcomes)
```

#### Play a Game
```python
from montecarlo_simulator.montecarlo import Game

# Create two dice
die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
die2 = Die(np.array([1, 2, 3, 4, 5, 6]))

# Create a game with two dice
game = Game([die1, die2])

# Play the game 5 times
game.play(5)

# Display the results in wide format
print(game.show('wide'))
```

#### Analyze a Game
```python
from montecarlo_simulator.montecarlo import Analyzer

# Analyze the results of the game
analyzer = Analyzer(game)

# Calculate the number of jackpots
jackpots = analyzer.jackpot()
print(f"Number of jackpots: {jackpots}")

# Get face counts per roll
face_counts = analyzer.face_counts_per_roll()
print(face_counts)
```

---

## API Description
### Die Class
A class representing a die with weighted sides.

#### Methods:
- `__init__(self, faces: np.ndarray)`: Initialize the die with unique faces.
- `change_weight(self, face, new_weight)`: Change the weight of a specific face.
- `roll(self, rolls=1)`: Roll the die a specified number of times.
- `show(self)`: Display the current state of the die.

### Game Class
A class for simulating a game using multiple dice.

#### Methods:
- `__init__(self, dice: list)`: Initialize the game with a list of Die objects.
- `play(self, rolls=1)`: Roll all dice a specified number of times.
- `show(self, form='wide')`: Display the results of the most recent game in wide or narrow format.

### Analyzer Class
A class for analyzing the outcomes of a game.

#### Methods:
- `__init__(self, game: Game)`: Initialize the analyzer with a Game object.
- `jackpot(self)`: Calculate the number of rolls where all dice have the same face.
- `face_counts_per_roll(self)`: Calculate face counts for each roll.
- `combo_count(self)`: Count distinct combinations of faces rolled.
- `permutation_count(self)`: Count distinct permutations of faces rolled.
- `scrabble_word_analysis(self, word_list: list)`: Analyze rolls to find valid Scrabble words.
- `letter_frequency_analysis(self, letter_frequencies: dict)`: Compare rolled letter frequencies to expected frequencies.

---

Feel free to reach out for any further assistance or suggestions for improvements!

