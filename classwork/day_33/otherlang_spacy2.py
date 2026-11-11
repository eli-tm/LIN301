import sys
sys.path.append("../../data")
from lin301 import *

import unicodedata
import spacy
nlp_it = spacy.load("it_core_news_sm")

### Activity 1: Which script?
el = "Η γάτα κοιμάται στον καναπέ."
ru = "Кошка спит на диване."
ja2 = "猫はソファで寝ます。"
# count the letters in each script
for sentence in [el, ru, ja2]:
    rows = []
    for c in sentence:
        if c.isalpha():
            rows.append({"char": c, "script": script_of(c)})
    print(pd.DataFrame(rows).groupby("script").size().to_dict())

