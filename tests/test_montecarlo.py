#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


import unittest
import numpy as np
import pandas as pd
from montecarlo_simulator.montecarlo import Die, Game, Analyzer

class TestDie(unittest.TestCase):
    def setUp(self):
        self.faces = np.array([1, 2, 3, 4, 5, 6])
        self.die = Die(self.faces)

    def test_initialization(self):
        with self.assertRaises(TypeError):
            Die([1, 2, 3])  # Not a NumPy array
        with self.assertRaises(ValueError):
            Die(np.array([1, 1, 2]))  # Non-unique faces

    def test_change_weight(self):
        self.die.change_weight(1, 3.0)
        self.assertEqual(self.die.show().at[1, 'weight'], 3.0)
        with self.assertRaises(IndexError):
            self.die.change_weight(7, 2.0)  # Face does not exist
        with self.assertRaises(TypeError):
            self.die.change_weight(1, 'high')  # Invalid weight type

    def test_roll(self):
        outcomes = self.die.roll(10)
        self.assertEqual(len(outcomes), 10)
        self.assertTrue(all(face in self.faces for face in outcomes))

    def test_show(self):
        state = self.die.show()
        self.assertEqual(state.shape, (6, 1))  # 6 faces, 1 weight column


class TestGame(unittest.TestCase):
    def setUp(self):
        self.die1 = Die(np.array(['A', 'B', 'C', 'D', 'E', 'F']))
        self.die2 = Die(np.array(['A', 'B', 'C', 'D', 'E', 'F']))
        self.game = Game([self.die1, self.die2])

    def test_initialization(self):
        with self.assertRaises(TypeError):
            Game(['not_a_die'])  # Invalid list of Die objects

    def test_play(self):
        self.game.play(5)
        results = self.game.show()
        self.assertEqual(results.shape, (5, 2))  # 5 rolls, 2 dice

    def test_show(self):
        self.game.play(5)
        wide_results = self.game.show('wide')
        self.assertEqual(wide_results.shape, (5, 2))
        narrow_results = self.game.show('narrow')
        self.assertEqual(narrow_results.shape, (10, 1))  # 5 rolls * 2 dice
        with self.assertRaises(ValueError):
            self.game.show('invalid')  # Invalid form argument


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        die1 = Die(np.array(['A', 'B', 'C']))
        die2 = Die(np.array(['A', 'B', 'C']))
        self.game = Game([die1, die2])
        self.game.play(5)
        self.analyzer = Analyzer(self.game)

    def test_initialization(self):
        with self.assertRaises(TypeError):
            Analyzer('not_a_game')  # Not a Game object

    def test_jackpot(self):
        jackpots = self.analyzer.jackpot()
        self.assertTrue(isinstance(jackpots, (int, np.integer)), f"Expected jackpots to be an int, but got {type(jackpots)}")
        self.assertGreaterEqual(jackpots, 0)

    def test_face_counts_per_roll(self):
        face_counts = self.analyzer.face_counts_per_roll()
        self.assertEqual(face_counts.shape[0], 5)  # 5 rolls
        self.assertTrue(all(col in ['A', 'B', 'C'] for col in face_counts.columns))

    def test_combo_count(self):
        combo_counts = self.analyzer.combo_count()
        self.assertIsInstance(combo_counts, pd.DataFrame)

    def test_permutation_count(self):
        permutation_counts = self.analyzer.permutation_count()
        self.assertIsInstance(permutation_counts, pd.DataFrame)

    def test_scrabble_word_analysis(self):
        scrabble_words = ['AA', 'BB', 'CC']
        analysis = self.analyzer.scrabble_word_analysis(scrabble_words)
        self.assertEqual(analysis.shape[0], 5)  # 5 rolls
        self.assertIn('Is_Valid_Word', analysis.columns)

    def test_letter_frequency_analysis(self):
        letter_frequencies = {'A': 8, 'B': 3, 'C': 5}
        frequency_analysis = self.analyzer.letter_frequency_analysis(letter_frequencies)
        self.assertTrue(all(col in ['Rolled_Count', 'Expected_Frequency'] for col in frequency_analysis.columns))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




