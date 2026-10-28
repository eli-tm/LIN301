import os
import re

def ttr(words):
    ttr = len(set(words))/len(words)
    return ttr

def ttr_first(words, n=10000):  # default to the first 10,000 words
    return len(set(words[:n])) / len(words[:n])

def avg_word_len(words):
    wl = 0
    for w in words:
        wl += len(w)
    return wl/len(words)

def load_words(filename):
    with open("../../data/gutenberg/" + filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    while not lines[0].startswith("*** START"):
        lines = lines[1:]
    lines = lines[1:]

    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]
    lines = lines[:-1]

    text = "".join(lines)
    words = re.split(r"[\W]+", text.lower())
    words = [w for w in words if w != ""]
    return words

def report(title, words):
    ttr = len(set(words)) / len(words)
    ttr_10000 = len(set(words[:10000])) / len(words[:10000])

    letters = 0
    for w in words:
        letters += len(w)

    print(title, "TTR:", ttr)
    print(title, "TTR (10,000 words):", ttr_10000)
    print(title, "Average Word Length:", letters / len(words))
    return ttr_10000