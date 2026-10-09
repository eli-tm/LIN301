from collections import Counter

words = "the cat saw the dog and the dog saw the cat".split()
print(Counter(words).most_common(3))

words_tokens = len(words)
words_types = len(set(words))
words_ttr = words_types/words_tokens

print(words_tokens, words_types, words_ttr)

print("========")
x = 0
while x < 10:
    print(x, "is less than 10.")
    x = x + 1

name = "The University of Kentucky"
while name:
    print("|" + name + "|")
    name = name[0:-1]

print("====Activity====")
messy = "Really?!?!"
extra = "?!"
while messy[-1] in extra:
    messy = messy[:-1]

print(messy)

print("========")
with open("../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
    alice_lines = f.readlines()

while not alice_lines[0].startswith("*** START"):
    alice_lines = alice_lines[1:]     # chop off the first line
alice_lines = alice_lines[1:]         # chop off the *** START line itself

print(alice_lines[0:5])

while not alice_lines[-1].startswith("*** END"):
    alice_lines = alice_lines[:-1]    # chop off the last line
alice_lines = alice_lines[:-1]        # chop off the *** END line itself

alice_text = "".join(alice_lines)

print(alice_lines[-5:])

import re

alice_words = re.split(r"[\W]+", alice_text.lower())
alice_words = [w for w in alice_words if w != ""]