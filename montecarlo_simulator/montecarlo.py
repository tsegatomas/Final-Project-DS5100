import os
import numpy as np
import pandas as pd

class Die:
    """
    A class representing a die with N sides, each side having a unique symbol and weight.
    """
    def __init__(self, faces):
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array.")
        if len(faces) != len(set(faces)):
            raise ValueError("Faces must be distinct values.")
        
        self._faces = faces
        self._weights = np.ones(len(faces))  # Default weight of 1.0 for each face
        self._die_df = pd.DataFrame({
            'face': faces,
            'weight': self._weights
        }).set_index('face')

    def change_weight(self, face, new_weight):
        if face not in self._die_df.index:
            raise IndexError("Face value not found in die.")
        if not isinstance(new_weight, (int, float)) or new_weight < 0:
            raise TypeError("Weight must be a positive numeric value.")
        
        self._die_df.at[face, 'weight'] = float(new_weight)

    def roll(self, rolls=1):
        return self._die_df.sample(n=rolls, weights='weight', replace=True).index.tolist()
    
    def show(self):
        return self._die_df.copy()


class Game:
    """
    A class representing a game consisting of rolling one or more dice.
    """
    def __init__(self, dice):
        if not isinstance(dice, list) or not all(isinstance(die, Die) for die in dice):
            raise TypeError("All elements must be Die objects.")
        self.dice = dice
        self._results = None

    def play(self, rolls=1):
        results = {f"Die_{i}": die.roll(rolls) for i, die in enumerate(self.dice)}
        self._results = pd.DataFrame(results)
        self._results.index.name = 'Roll'

    def show(self, form='wide'):
        if self._results is None:
            raise ValueError("No results available. Please play the game first.")
        if form == 'wide':
            return self._results
        elif form == 'narrow':
            return self._results.stack().to_frame('Outcome')
        else:
            raise ValueError("Invalid form. Use 'wide' or 'narrow'.")


class Analyzer:
    """
    A class for analyzing the results of a game of dice.
    """
    def __init__(self, game):
        if not isinstance(game, Game):
            raise TypeError("Input must be a Game object.")
        self.game = game
        self.results = game.show(form='wide')

    def jackpot(self):
        return (self.results.nunique(axis=1) == 1).sum()

    def face_counts_per_roll(self):
        return self.results.apply(pd.Series.value_counts, axis=1).fillna(0)

    def combo_count(self):
        sorted_rolls = self.results.apply(lambda x: tuple(sorted(x)), axis=1)
        return sorted_rolls.value_counts().to_frame('Count')

    def permutation_count(self):
        perm_rolls = self.results.apply(lambda x: tuple(x), axis=1)
        return perm_rolls.value_counts().to_frame('Count')

    def scrabble_word_analysis(self, word_list):
        valid_words = []
        for roll in self.results.apply(lambda x: ''.join(sorted(x)), axis=1):
            if roll in word_list:
                valid_words.append(True)
            else:
                valid_words.append(False)
        
        return pd.DataFrame({'Roll': self.results.index, 'Is_Valid_Word': valid_words})

    def letter_frequency_analysis(self, letter_frequencies):
        rolled_letter_counts = self.results.apply(pd.Series.value_counts).sum().fillna(0)
        comparison = pd.DataFrame({'Rolled_Count': rolled_letter_counts})
        comparison['Expected_Frequency'] = comparison.index.map(letter_frequencies)
        comparison['Expected_Frequency'] = comparison['Expected_Frequency'].fillna(0)
        return comparison


# Adjust file paths for scrabble words and English letter frequencies
current_dir = os.path.dirname(__file__)
scrabble_words_path = os.path.join(current_dir, 'scrabble_words.txt')
english_letters_path = os.path.join(current_dir, 'english_letters.txt')

# Load scrabble words
try:
    with open(scrabble_words_path) as f:
        scrabble_words = [line.strip() for line in f]
except FileNotFoundError:
    raise FileNotFoundError(f"Could not find scrabble_words.txt at {scrabble_words_path}")

# Load English letter frequencies
try:
    letter_frequencies = {}
    with open(english_letters_path) as f:
        for line in f:
            letter, frequency = line.strip().split()
            letter_frequencies[letter] = float(frequency)
except FileNotFoundError:
    raise FileNotFoundError(f"Could not find english_letters.txt at {english_letters_path}")
