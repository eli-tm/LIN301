import re
import pandas as pd

with open("hw5_raw.txt", "r", encoding="utf-8") as f:
    formentera_lines = f.readlines()    # opening the txt as a list of lines

print(formentera_lines[0:20])

formentera_text = "".join(formentera_lines)     # joining the list

print(formentera_text)
songs_intro = re.split(r"\[Intro\]", formentera_text)   # splitting the songs by intro
songs_div = "".join(songs_intro)

songs = re.split(r"\n\[verse 1\]", formentera_text.lower()) # splitting the songs by verse 1 (all songs have verse 1 but not all songs have intro)
print(songs[0])
print(len(songs))
print(songs)

# creating 1 row per word with its song number, deleting [chorus], etc.
rows = []
song_num = 0

for song in songs:
    song_num += 1
    lyrics = re.split(r"[\n]+", song)
    lyrics = [w for w in lyrics if w != ""]
    lyrics = [w for w in lyrics if not w.startswith("[")]
    for w in lyrics:
        rows.append({"lyric": w, "track": song_num})

# saving as data frame
formentera_df = pd.DataFrame(rows)
print(formentera_df.head())

# adding columns
# add name of song indexed by track number
names = ["Doomscroller", "All Comes Crashing", "What Feels Like Eternity", "Formentera", "Enemies of the Ocean", "I Will Never Settle", "Oh Please", "Paths in the Sky"]
for s, i in formentera_df.items():
    if formentera_df[formentera_df["track"]] == 1:
        formentera_df["song"] = names[0]

print(formentera_df.head())

# add another column of verse/chorus/bridge/intro/outro (modify splitting step to create another value?)

# add 3 additional columns:
    # number of words per lyric
    # if line is unique (to entire album) (values: unique, repeats)
    # T/F if line contains a content word from its song title

formentera_df.to_csv("hw5_trainor_eli.csv", index=False, encoding="utf-8-sig")
