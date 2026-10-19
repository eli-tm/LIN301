print("====Review Activity====")
import pandas as pd
import re

root    = ["*bʰer-", "*ĝenh₁-", "*ped-", "*doh₃-"]
meaning = ["to carry", "to beget", "foot", "to give"]
latin   = ["ferō", "gignō", "pēs", "dō"]
greek   = ["pʰérō", "gígnomai", "poús", "dídōmi"]
english = ["bear", "kin", "foot", "donate"]

roots_rows = []
for r, m, l, g, e in zip(root, meaning, latin, greek, english):
    roots_rows.append({
    "root": r, 
    "meaning": m,
    "latin": l, 
    "greek": g, 
    "english": e
})

roots_df = pd.DataFrame(roots_rows)

roots_df.to_csv("pie_roots.csv", index=False, encoding="utf-8-sig")

print("========")
import re
import pandas as pd

with open("../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
    alice_lines = f.readlines()

while not alice_lines[0].startswith("*** START"):
    alice_lines = alice_lines[1:]
alice_lines = alice_lines[1:]

while not alice_lines[-1].startswith("*** END"):
    alice_lines = alice_lines[:-1]
alice_lines = alice_lines[:-1]

alice_text = "".join(alice_lines)

##### splitting into chapters
import re

chapters = re.split(r"\nCHAPTER [IVXL]+", alice_text)

chapters = chapters[1:]     # chop of table of contents

#####
rows = []
chapter_num = 0

for chapter in chapters:
    chapter_num += 1
    words = re.split(r"[\W]+", chapter.lower())
    words = [w for w in words if w != ""]
    for w in words:
        rows.append({"word": w, "chapter": chapter_num})

alice_df = pd.DataFrame(rows)

#####
print(alice_df.head()) #down the rabbit hole
print(alice_df.tail()) #the end
print(len(alice_df))

#### Activity start:
print(len(alice_df))        # how many words are in alice
print(alice_df.head(30))    # print first 30 words (rows)

words = alice_df["word"]    # store "word" collumn in a variable

print("========")
alice_df[alice_df["word"] == "queen"]       # which rows are "queen"
alice_df[alice_df["word"].str.endswith("ly")]   #which rows end with -ly


print("====Activity Part 2====")
print(len(alice_df[alice_df["word"] == "alice"]))        # how many times alice appears in the book
ing = alice_df[alice_df["word"].str.endswith("ing")]     # find words that end in -ing
print(ing)
un = alice_df[alice_df["word"].str.startswith("un")]      # find words that start witn un-
print(un)

print("========")
un = un[un["word"] != "under"]                         # filter out "under" from un- words

alice_df[(alice_df["word"] == "queen") & (alice_df["chapter"] == 8)]        # find the word queen only if it appears in chapter 8
alice_df[(alice_df["word"] == "king") | (alice_df["word"] == "queen")]      # find king or queen
alice_df[((alice_df["word"] == "king") | (alice_df["word"] == "queen")) & (alice_df["chapter"] == 8)]   # either king or queen only in chapter 8
alice_df[(alice_df["word"].isin(["king", "queen"])) & (alice_df["chapter"] == 8)]       # same as above but shorter

stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t", "am"]
alice_df[alice_df["word"].isin(stopwords)]      # finds all stopwords

content = alice_df[~alice_df["word"].isin(stopwords)]   # finds all content words

print("====Activity Part 3====")
alice_df[(alice_df["word"].str.startswith("un")) & (alice_df["chapter"] == 1)]      # how many words in chapter 1 start with un-
alice_df[(alice_df["word"].isin(["king", "queen"])) & (alice_df["chapter"] == 12)]      # how many times does king or queen appear in chapter 12
print(len(content))    # how many words are content words
print(len(content) / len(words))    # what fraction of content words are the entire word count

print("====Counting====")
alice_df["word"].value_counts()     # shows the top words
content["word"].value_counts().head(10)     # shows the top 10 content words
