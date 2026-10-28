print("input = argument; output = return")
import re
import pandas as pd
print(round(0.15625, 2))
print(re.split(r"[\W]+", "Down the Rabbit-Hole"))

print("====Making Functions====")
def pluralize(noun):
    plural = noun + "s"
    return plural

print(pluralize("cat"))

print("====Activity====")
# 1 (past tense)
def past_tense(verb):
    past = verb + "ed"
    return past
print(past_tense("walk"))
print(past_tense("talk"))
print(past_tense("jump"))
# 2 (ttr)
def ttr(words):
    ttr = len(set(words))/len(words)
    return ttr
test = ["the", "cat", "saw", "the", "dog"]
print(ttr(test))

print("========")
def ttr_print(words):
    print(len(set(words)) / len(words)) # this doesn't STORE the value and doesn't work for calculations

def ttr_return(words):
    return len(set(words)) / len(words)

# both of the above give the same value

def ttr_first(words, n):    
    return len(set(words[:n])) / len(words[:n])
print(ttr_first(test, 3))
print(ttr_first(test, 5))

def ttr_first(words, n=10000):  # default to the first 10,000 words
    return len(set(words[:n])) / len(words[:n])

print("====Activity====")
# function for average word length
def avg_word_len(words):
    wl = 0
    for w in words:
        wl += len(w)
    return wl/len(words)

print(avg_word_len(["a", "bb", "ccc"]))

print("====Simplifying Detective Gut====")
def load_words(filename):
    with open("../../data/gutenberg" + filename, "r", encoding="utf-8") as f:
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
