# 🐍 Python Challenge #12 — Count Items in a List
Overview

Counting how often items appear in a list is one of the most common patterns in programming.
In this challenge, you’ll write a function that returns a frequency dictionary, mapping each unique item to the number of times it occurs.

This challenge completes the Beginner Track by bringing together lists, loops, dictionaries, and input validation.

# 🧠 The Challenge

Write a function that counts how many times each item appears in a list.

Function Signature
def count_items(items: list) -> dict:
    ...

# ✅ Rules

The input must be a list

Raise TypeError if the input is not a list
Each item in the list must be hashable
Raise TypeError if an item cannot be used as a dictionary key

Return a dictionary where:
Keys are unique items from the list
Values are the number of times each item appears
Return an empty dictionary for an empty list

# 📌 Examples

count_items([1, 2, 2, 3])
-> {1: 1, 2: 2, 3: 1}

count_items(["a", "b", "a"])
 -> {"a": 2, "b": 1}

count_items([])
-> {}

# ❌ Invalid Input Examples
count_items("abc")          # TypeError
count_items(None)           # TypeError
count_items([1, [], 2])     # TypeError (unhashable item)

#💡 Hints

Use a dictionary to store counts
Check if an item already exists before incrementing
Remember: not all Python objects are hashable

# 🧪 Running the Tests

This challenge includes automated tests using pytest.

Install pytest (if needed)
pip install pytest

Run tests
pytest -q

# 📁 Project Structure
.
├── challenge_12_count_items.py
├── test_challenge_12_count_items.py
└── README.md

# 🎯 What This Challenge Teaches

Iterating through lists
Using dictionaries as counters
Understanding hashable vs unhashable types
Writing predictable, defensive code

# 🚀 Bonus Ideas

Ignore case when counting strings
Sort the result by frequency
Rebuild the solution using collections.Counter
Count items across multiple lists

# 🏁 Beginner Track Complete

With this challenge, you’ve completed the SolveWithPython Beginner Track.

You now have hands-on experience with:

Strings
Lists
Conditionals
Dictionaries
Validation
Frequency patterns

# 🔗 Learn More

This challenge is part of the [SolveWithPython](https://solvewithpython.com/) series.

Explore more challenges at:
👉 https://solvewithpython.com
