import os
import re
HERE = os.path.dirname(__file__)   # the folder lin301.py lives in: data/

# report ttr
def ttr(words):
    ttr = len(set(words))/len(words)
    return ttr

# report ttr of first 10,000 words
def ttr_first(words, n=10000):  # default to the first 10,000 words
    return len(set(words[:n])) / len(words[:n])

# report average word length
def avg_word_len(words):
    wl = 0
    for w in words:
        wl += len(w)
    return wl/len(words)

# load txt:
def load_text(filename):
    with open(os.path.join(HERE, "gutenberg", filename), "r", encoding="utf-8") as f:
        lines = f.readlines()

    while not lines[0].startswith("*** START"):
        lines = lines[1:]
    lines = lines[1:]
    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]
    lines = lines[:-1]

    return "".join(lines)

# clean txt
def load_words(filename):
    text = load_text(filename)
    words = re.split(r"[\W_]+", text.lower())
    return [w for w in words if w != ""]


# report all ttr info of txt
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

def report(title, words):   # same way to do the above but shorter
    print(title, "TTR:", ttr(words))
    print(title, "TTR (10,000 words):", ttr_first(words))
    print(title, "Average Word Length:", avg_word_len(words))
    return ttr_first(words)

# report rate of -ly words per 1,000 words
def ly_rate(words):
    ly = 0
    for w in words:
        if w.endswith("ly"):
            ly += 1
    return ly/len(words) * 1000