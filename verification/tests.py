"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

import random

TESTS = {
    "Basics": [],
    "Small": [],
    "Big": []
}

def addTest(c, i, a):
    TESTS[c].append({"input": i, "answer": a})

addTest("Basics", [2, 4, 3, [0, 0, 0, 0]], ????)

