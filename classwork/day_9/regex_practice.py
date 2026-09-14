import re                                             # loads Python's regex toolkit

with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:  # opens alice.txt for reading
    text = f.read()                                   # reads the whole file into one string, called `text`