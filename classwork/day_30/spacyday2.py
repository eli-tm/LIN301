import sys
sys.path.append("../../data")
from lin301 import *

import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

# splitting strings into sentences:
doc = nlp("I am delighted to be here today. We meet in an hour of change and challenge. Do cats eat bats?")
for sent in doc.sents:
    print(sent.text)

### dependencies!!
# get POS and syntactic properties:
doc = nlp("Do cats eat bats?")

for token in doc:
    print(token.text, token.dep_, token.head.text)

# show syntactic dependencies visually:
from spacy import displacy

doc = nlp("Do cats eat bats?")
svg = displacy.render(doc, style="dep")
with open("cats_eat_bats.svg", "w", encoding="utf-8") as f:
    f.write(svg)

# generating children:
doc = nlp("The Mock Turtle sang a song about soup.")
for token in doc:
    print(token.text, token.dep_, [child.text for child in token.children])

print("===Activity: Group by sentence length====")
alice_sp = book_to_spacy_df("alice.txt", "Alice", nlp)
# find average sentence length:
print(alice_sp.groupby(["chapter", "sentence"]).size().mean())
# compare to mansfield park:
mp_sp = book_to_spacy_df("mansfield_park.txt", "Mansfield", nlp)
print(mp_sp.groupby(["chapter", "sentence"]).size().mean())
# find longest sentence in Alice:
print(alice_sp.groupby(["chapter", "sentence"]).size().sort_values())

print("===Actiity: Make another visualization====")
doc = nlp("Do bats eat cats?")
svg = displacy.render(doc, style="dep")
with open("bats_eat_cats.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("===Activity: print dependencies and headers===")
doc = nlp("The Hatter dropped his teacup on the floor.")
for token in doc:
    print(token.text, token.dep_, [child.text for child in token.children])
svg = displacy.render(doc, style="dep")
with open("the_hatter.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("====Activity: who does what====")
alice_svo = book_to_svo_df("alice.txt", "Alice", nlp)
alice_svo.head()
# 10 most common verbs:
alice_svo.groupby("verb").size().sort_values(ascending=False).head(10)
# what does the queen do?
queen = alice_svo[alice_svo["subject"] == "Queen"]
queen.groupby("verb").size().sort_values(ascending=False).head(8)
# what does the hatter do?
hatter = alice_svo[alice_svo["subject"] == "Hatter"]
hatter.groupby("verb").size().sort_values(ascending=False).head(8)
# what doese the rabbit do?
rabbit = alice_svo[alice_svo["subject"] == "Rabbit"]
rabbit.groupby("verb").size().sort_values(ascending=False).head(8)
# what gets said?
said = alice_svo[alice_svo["verb"] == "said"]
said.groupby("object").size().sort_values(ascending=False)

print("===Activity: make you own group====")
group = ['rose', 'sword', 'heart', 'head', 'eye', 'crown', 'king']
print(alice_svo[alice_svo["object"].isin(group)])