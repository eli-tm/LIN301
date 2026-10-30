import sys
sys.path.append("../../data")
from lin301 import *    # this allows you to call up all of the functions in the file, without using the lin301. initial part
import re
import pandas as pd

oz_words = load_words("oz.txt")
print('The TTR of "The Wonderful Wizard of Oz" for the first 1000 words is: ', ttr_first(oz_words))
print('The average word length in "The Wonderful Wizard of Oz" is: ', avg_word_len(oz_words))

alice_words = load_words("alice.txt")
mansfield_words = load_words("mansfield_park.txt")

print("====LY Rate Fuction====")
def ly_rate(words):
    ly = 0
    for w in words:
        if w.endswith("ly"):
            ly += 1
    return ly/len(words) * 1000

print(ly_rate(["quickly", "fox", "only", "the"]))

print("====Book to DF function====")

def book_to_df(filename, label):
    text = load_text(filename)

    chapters = re.split(r"\nCHAPTER [IVXL]+", text)
    chapters = chapters[1:]

    rows = []
    chapter_num = 0
    for chapter in chapters:
        chapter_num += 1
        words = re.split(r"[\W_]+", chapter.lower())
        words = [w for w in words if w != ""]
        for w in words:
            rows.append({"word": w, "chapter": chapter_num})

    df = pd.DataFrame(rows)
    df["text"] = label
    return df

alice_df = book_to_df("alice.txt", "alice")
mp_df = book_to_df("mansfield_park.txt", "mansfield")
print(len(alice_df), alice_df["chapter"].nunique())
print(len(mp_df), mp_df["chapter"].nunique())
