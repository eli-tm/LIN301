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
print(formentera_df.tail())

# adding columns
# add name of song indexed by track number
names = ["Doomscroller", "All Comes Crashing", "What Feels Like Eternity", "Formentera", "Enemies of the Ocean", "I Will Never Settle", "False Dichotomy", "Oh Please", "Paths in the Sky"]
track_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

song_names = dict(zip(track_num, names)) # creating a dict of track: song

# making a dict within a list:
song_rows = []
for track, name in song_names.items():
    song_rows.append({
        "track": track,
        "song": name
    })

print(song_rows)

# making a DataFrame with pandas:
songs_df = pd.DataFrame(song_rows)

print(songs_df.head())

formentera2_df = pd.merge(formentera_df, songs_df, on="track", how="outer") # merging 2 dataframes from a shared column

# number of words per lyric:
# Source - https://stackoverflow.com/a/51325605
# Posted by altabq, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-01, License - CC BY-SA 4.0

formentera2_df['word_count'] = formentera2_df['lyric'].str.count(' ') + 1

# if line is unique (to entire album)
# Source - https://stackoverflow.com/a/66869743
# Posted by jezrael, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-01, License - CC BY-SA 4.0

formentera2_df['unique'] = ~formentera2_df['lyric'].duplicated(keep=False)

# T/F if line contains a content word from its song title
title_content = ["doomscroller", "crashing", "feels", "eternity", "formentera", "enemies", "ocean", "settle", "paths", "sky"] # used https://app.readable.com/text/stopwords/

formentera2_df['contains_album_word'] = formentera2_df['lyric'].str.contains("doomscroller" or "crashing" or "feels" or "eternity" or "formentera" or "enemies" or "ocean" or "settle" or "false" or "dichotomy" or "paths" or "sky")

print(formentera2_df.head())
print(formentera2_df.tail())
formentera2_df.to_csv("hw5_trainor_eli.csv", index=False, encoding="utf-8-sig")
