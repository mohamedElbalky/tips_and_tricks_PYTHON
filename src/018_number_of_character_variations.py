
"""
    I don't get it!!!!!!!!!!!!
"""

import math


skills = [
    'HTML',
    'CSS',
    'JS',
    'JS',
    'HTML',
    'CSS',
    'JS',
    'JS'
]

num_skills = len(skills)
print("Number of Skills: ", num_skills)

variations = math.comb(num_skills, 3)
print("\nNumber of Possible Skill Combinations (with Repetition): ", variations)
