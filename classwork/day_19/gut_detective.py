print("====King in Yellow====")

with open("../../data/gutenberg/king_yellow.txt", "r", encoding="utf-8") as f:
    king_lines = f.readlines()

while not king_lines[0].startswith("                      THE REPAIRER OF REPUTATIONS"):       #the heading of the first chapter
    king_lines = king_lines[1:]     
king_lines = king_lines[1:]         

print(king_lines[0:5])

while not king_lines[-1].startswith("*** END"):
    king_lines = king_lines[:-1]    # chop off the last line
king_lines = king_lines[:-1]        # chop off the *** END line itself

king_text = "".join(king_lines)

print(king_lines[-5:])

import re

king_words = re.split(r"[\W]+", king_text.lower())
king_words = [w for w in king_words if w != ""]

print(king_words[0:200])


print("====The Wizard of Oz====")
with open("../../data/gutenberg/oz.txt", "r", encoding="utf-8") as f:
    oz_lines = f.readlines()

while not oz_lines[0].startswith("The Cyclone"):    #The heading of the first chapter
    oz_lines = oz_lines[1:]     
oz_lines = oz_lines[1:]         

print(oz_lines[0:5])

while not oz_lines[-1].startswith("*** END"):
    oz_lines = oz_lines[:-1]    # chop off the last line
oz_lines = oz_lines[:-1]        # chop off the *** END line itself

oz_text = "".join(oz_lines)

print(oz_lines[-5:])

import re

oz_words = re.split(r"[\W]+", oz_text.lower())
oz_words = [w for w in oz_words if w != ""]

print(oz_words[0:200])

print("====Explore====")
king_tokens = len(king_words)
king_types = len(set(king_words))
king_ttr = king_types/king_tokens

oz_tokens = len(oz_words)
oz_types = len(set(oz_words))
oz_ttr = oz_types/oz_tokens

print("The King in Yellow has", king_tokens, "words,", king_types, "unique words, and a", king_ttr, "TTR.")
print("The Wizard of Oz has", oz_tokens, "words,", oz_types, "unique words, and a", oz_ttr, "TTR.")
print("     The King in Yellow has a richer vocabulary.")

king_ttr_10000 = len(set(king_words[:10000])) / len(king_words[:10000])
oz_ttr_10000 = len(set(oz_words[:10000])) / len(oz_words[:10000])

print("The King in Yellow TTR (10,000 words):", king_ttr_10000)
print("The Wizard of Oz TTR (10,000 words):", oz_ttr_10000)
print("     The King in Yellow has a richer vocabulary within 10,000 words.")

king_wc = 0
for w in king_words:
    king_wc += len(w)
king_awl = king_wc/len(king_words)

oz_wc = 0
for w in oz_words:
    oz_wc += len(w)
oz_awl = oz_wc/len(oz_words)

print("The King in Yellow has an average word length of", king_awl, "characters.")
print("The Wizard of Oz has an average word length of", oz_awl, "characters.")

print("========")
from collections import Counter
import matplotlib.pyplot as plt

king_freqs = [pair[1] for pair in Counter(king_words).most_common()]
king_ranks = range(1, len(king_freqs) + 1)    # 1, 2, 3, ... up to the number of words

plt.plot(king_ranks, king_freqs)
plt.title("Rank vs. Frequency")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale("log")
plt.yscale("log")
#plt.show()

oz_freqs = [pair[1] for pair in Counter(oz_words).most_common()]
oz_ranks = range(1, len(oz_freqs) + 1)    # 1, 2, 3, ... up to the number of words

plt.plot(oz_ranks, oz_freqs)
plt.title("Rank vs. Frequency")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale("log")
plt.yscale("log")
#plt.show()

print("====LY====")
#words ending in -ly per 1,000 words
ly = "ly"
king_ly = set()     #includes "early"!
for w in king_words:
    if w.endswith(ly):
        king_ly.add(w)
print("The King in Yellow has", len(king_ly), "words that end in -ly.")
king_ly_rate = len(king_ly) / len(king_words) * 1000
print("The King in Yellow has", king_ly_rate, "-ly words per 1000 words.")

oz_ly = set()       #includes "family"!
for w in oz_words:
    if w.endswith(ly):
        oz_ly.add(w)
print("The Wizard of Oz has", len(oz_ly), "words that end in -ly.")
oz_ly_rate = len(oz_ly) / len(oz_words) * 1000
print("The Wizard of Oz has", oz_ly_rate, "-ly words per 1000 words.")

print("====TION====")
king_tion = set()
for w in king_words:
    if w.endswith("tion"):
        king_tion.add(w)
print("The King in Yellow has", len(king_tion), "words that end in -tion")
king_tion_rate = len(king_tion) / len(king_words) * 1000
print("The King in Yellow has", king_tion_rate, "-tion words per 1000 words.")

oz_tion = set()
for w in oz_words:
    if w.endswith("tion"):
        oz_tion.add(w)
print("The Wizard of Oz has", len(oz_tion), "words that end in -tion")
oz_tion_rate = len(oz_tion) / len(oz_words) * 1000
print("The Wizard of Oz has", oz_tion_rate, "-tion words per 1000 words.")

print("====MENT====")
king_ment = set()
for w in king_words:
    if w.endswith("ment"):
        king_tion.add(w)
print("The King in Yellow has", len(king_ment), "words that end in -ment")
king_ment_rate = len(king_ment) / len(king_words) * 1000
print("The King in Yellow has", king_ment_rate, "-ment words per 1000 words.")
print(king_ment, len(king_ment))
