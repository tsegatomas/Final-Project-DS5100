import numpy as np
from montecarlo_simulator.montecarlo import Die, Game, Analyzer

# Test Die
try:
    die = Die(np.array(['A', 'B', 'C']))
    print("Die successfully created!")
except Exception as e:
    print(f"Die creation failed: {e}")

# Test Game
try:
    game = Game([die, die])
    game.play(10)  # Play the game with 10 rolls
    print("Game successfully created!")
except Exception as e:
    print(f"Game creation failed: {e}")

# Test Analyzer
try:
    analyzer = Analyzer(game)
    print("Analyzer successfully created!")
except Exception as e:
    print(f"Analyzer creation failed: {e}")


