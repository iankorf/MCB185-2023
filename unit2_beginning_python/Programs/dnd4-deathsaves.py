# dnd4-deathsaves.py

# Death saves are a little different than normal saving throws. If your
# health drops to 0 or below, you are unconscious and may die. Each time it
# is your turn, roll a d20 to determine if you get closer to life or fall
# deeper into death. If the number is less than 10, you record a "failure".
# If the number is 10 or greater, you record a "success". If you collect 3
# failures, you "die". If you collect 3 successes, you are "stable" but
# unconscious. If you are unlucky and roll a 1, it counts as 2 failures.
# If you're lucky and roll a 20, you gain 1 health and have "revived".
# Write a program that simulates death saves. What is the probability one
# dies, stabilizes, or revives?


"""
python3 dnd4-deathsaves.py
die: 0.405
stabilize: 0.414
revive: 0.181
"""
