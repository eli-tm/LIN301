print("====Review Activity====")
lang_info = {
    "Latin":    {"family": "Indo-European", "location": "Italy"},
    "Greek":    {"family": "Indo-European", "location": "Greece"},
    "Sanskrit": {"family": "Indo-European", "location": "India"},
    "Finnish":  {"family": "Uralic",        "location": "Finland"}
}
#print the family of Sanskrit:
print("The family of Sanskrit is", lang_info["Sanskrit"]["family"])
#print every Info-European lang along with its location
for lang, features in lang_info.items():
    if features["family"] == "Indo-European":
        print(lang, features["location"])

print("====Lists of Dicts====")
lexicon = [
    {"form": "bank", "pos": "noun", "gloss": "edge of a river"},
    {"form": "bank", "pos": "noun", "gloss": "place to keep money"},
    {"form": "bank", "pos": "verb", "gloss": "to tilt an airplane"}
]
for entry in lexicon:           #it's like a spreadsheet!
    print(entry["form"], "(" + entry["pos"] + "):", entry["gloss"])

#back to lang_info:
lang_rows = []

for lang, info in lang_info.items():
    lang_rows.append({
        "language": lang,
        "family": info["family"],
        "location": info["location"]
    })

print(lang_rows)

print("====Pandas!====")
import pandas as pd

lang_df = pd.DataFrame(lang_rows)
print(lang_df)

print("====Activity====")
consonant =  ["p", "b", "t", "d", "k", "g", "s", "z", "m", "n", "l", "r", "w", "j", "h"]
place = ["bilabial", "bilabial", "alveolar", "alveolar", "velar", "velar", "alveolar", "alveolar", "bilabial", "alveolar", "alveolar", "alveolar", "labial-velar", "palatal", "glottal"]
manner = ["stop", "stop", "stop", "stop", "stop", "stop", "fricative", "fricative", "nasal", "nasal", "lateral", "trill", "glide", "glide", "fricative"]
voice = ["voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiceless"]

cons_df = pd.DataFrame({
    "consonant": consonant,
    "place": place,
    "manner": manner,
    "voice": voice
})
print(cons_df)

print("====Saving to .csv====")
# save as a .csv:
# lang_df.to_csv("languages.csv", index=False, encoding="utf-8-sig")

# read the .csv:
check = pd.read_csv("languages.csv")
print(check)

# look at slides for pipeline for working with .csv

print("====Activity 2====")
forms     = ["aqua", "rosa", "amō", "canis", "magnus", "videō", "puella", "bonus", "dominus", "portō", "lupus", "longus"]
glosses   = ["water", "rose", "I love", "dog", "big", "I see", "girl", "good", "lord", "I carry", "wolf", "long"]
pos       = ["noun", "noun", "verb", "noun", "adj", "verb", "noun", "adj", "noun", "verb", "noun", "adj"]
syllables = [2, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 2]

# making a nested dict:
latin_lex = {}
for f, g, p, s in zip(forms, glosses, pos, syllables):
    latin_lex[f] = {"gloss": g, "pos": p, "syllables": s}

# making a dict within a list:
latin_rows = []
for word, info in latin_lex.items():
    latin_rows.append({
        "word": word,
        "gloss": info["gloss"],
        "pos": info["pos"],
        "syllables": info["syllables"]
    })

# making a DataFrame with pandas:
latin_df = pd.DataFrame(latin_rows)

# save it as a .csv:
latin_df.to_csv("latin_lex.csv", index=False, encoding="utf-8-sig")

# open the .csv:
latincsv = pd.read_csv("latin_lex.csv")
print(latincsv)