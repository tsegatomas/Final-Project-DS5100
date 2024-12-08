import os
import numpy as np
import pandas as pd

class Die:
    """
    A class representing a die with N sides, each side having a unique symbol and weight.

    Attributes:
        _faces (np.ndarray): An array containing the faces of the die.
        _weights (np.ndarray): An array containing the weights associated with each face.
        _die_df (pd.DataFrame): A private DataFrame storing faces and weights.
    """

    def __init__(self, faces):
        """
        Initialize the Die object with faces and default weights.

        Args:
            faces (np.ndarray): A NumPy array of unique symbols representing the faces of the die.

        Raises:
            TypeError: If faces is not a NumPy array.
            ValueError: If faces contain duplicate values.
        """
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
        """
        Change the weight of a specific face on the die.

        Args:
            face: The face whose weight is to be changed.
            new_weight (float): The new weight to assign to the face.

        Raises:
            IndexError: If the face is not found in the die.
            TypeError: If the new weight is not a positive numeric value.
        """
        if face not in self._die_df.index:
            raise IndexError("Face value not found in die.")
        if not isinstance(new_weight, (int, float)) or new_weight < 0:
            raise TypeError("Weight must be a positive numeric value.")

        self._die_df.at[face, 'weight'] = float(new_weight)

    def roll(self, rolls=1):
        """
        Roll the die one or more times.

        Args:
            rolls (int): Number of times the die should be rolled. Defaults to 1.

        Returns:
            list: A list of outcomes for each roll.
        """
        return self._die_df.sample(n=rolls, weights='weight', replace=True).index.tolist()

    def show(self):
        """
        Show the current state of the die.

        Returns:
            pd.DataFrame: A DataFrame with the faces and their respective weights.
        """
        return self._die_df.copy()


class Game:
    """
    A class representing a game consisting of rolling one or more dice.

    Attributes:
        dice (list): A list of Die objects used in the game.
        _results (pd.DataFrame): A private DataFrame storing the results of the game.
    """

    def __init__(self, dice):
        """
        Initialize the Game with a list of dice.

        Args:
            dice (list): A list of Die objects.

        Raises:
            TypeError: If the input is not a list of Die objects.
        """
        if not isinstance(dice, list) or not all(isinstance(die, Die) for die in dice):
            raise TypeError("All elements must be Die objects.")
        self.dice = dice
        self._results = None

    def play(self, rolls=1):
        """
        Play the game by rolling all dice a specified number of times.

        Args:
            rolls (int): Number of times to roll the dice.

        Returns:
            None
        """
        results = {f"Die_{i}": die.roll(rolls) for i, die in enumerate(self.dice)}
        self._results = pd.DataFrame(results)
        self._results.index.name = 'Roll'

    def show(self, form='wide'):
        """
        Show the results of the most recent play.

        Args:
            form (str): Format of the results, either 'wide' or 'narrow'. Defaults to 'wide'.

        Returns:
            pd.DataFrame: The results in the specified format.

        Raises:
            ValueError: If no results are available or the format is invalid.
        """
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

    Attributes:
        game (Game): The Game object to analyze.
        results (pd.DataFrame): The results of the game in wide format.
    """

    def __init__(self, game):
        """
        Initialize the Analyzer with a Game object.

        Args:
            game (Game): The Game object to analyze.

        Raises:
            TypeError: If the input is not a Game object.
        """
        if not isinstance(game, Game):
            raise TypeError("Input must be a Game object.")
        self.game = game
        self.results = game.show(form='wide')

    def jackpot(self):
        """
        Compute the number of jackpots (all faces are the same).

        Returns:
            int: The number of jackpots.
        """
        return (self.results.nunique(axis=1) == 1).sum()

    def face_counts_per_roll(self):
        """
        Compute how many times each face was rolled per event.

        Returns:
            pd.DataFrame: A DataFrame with face counts for each roll.
        """
        return self.results.apply(pd.Series.value_counts, axis=1).fillna(0)

    def combo_count(self):
        """
        Compute the distinct combinations of faces rolled, order-independent.

        Returns:
            pd.DataFrame: A DataFrame with combinations and their counts.
        """
        sorted_rolls = self.results.apply(lambda x: tuple(sorted(x)), axis=1)
        return sorted_rolls.value_counts().to_frame('Count')

    def permutation_count(self):
        """
        Compute the distinct permutations of faces rolled, order-dependent.

        Returns:
            pd.DataFrame: A DataFrame with permutations and their counts.
        """
        perm_rolls = self.results.apply(lambda x: tuple(x), axis=1)
        return perm_rolls.value_counts().to_frame('Count')

