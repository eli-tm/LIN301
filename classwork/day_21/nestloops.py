print("====TTR and Count Review====")

jfk = "This year’s space budget is three times what it was in January 1961, and it is greater than the space budget of the previous eight years combined. That budget now stands at $5,400,000 a year — a staggering sum, though somewhat less than we pay for cigarettes and cigars every year. Space expenditures will soon rise some more, from 40 cents per person per week to more than 50 cents a week for every man, woman and child in the United States, for we have given this program a high national priority — even though I realize that this is in some measure an act of faith and vision, for we do not now know what benefits await us. But if I were to say, my fellow citizens, that we shall send to the moon, 240,000 miles away from the control station in Houston, a giant rocket more than 300 feet tall, the length of this football field, made of new metal alloys, some of which have not yet been invented, capable of standing heat and stresses several times more than have ever been experienced, fitted together with a precision better than the finest watch, carrying all the equipment needed for propulsion, guidance, control, communications, food and survival, on an untried mission, to an unknown celestial body, and then return it safely to Earth, re-entering the atmosphere at speeds of over 25,000 miles per hour, causing heat about half that of the temperature of the sun — almost as hot as it is here today — and do all this, and do it right, and do it first before this decade is out — then we must be bold. I’m the one who is doing all the work, so we just want you to stay cool for a minute. [laughter] However, I think we’re going to do it, and I think that we must pay what needs to be paid. I don’t think we ought to waste any money, but I think we ought to do the job. And this will be done in the decade of the sixties. It may be done while some of you are still here at school at this college and university. It will be done during the term of office of some of the people who sit here on this platform. But it will be done. And it will be done before the end of this decade. I am delighted that this university is playing a part in putting a man on the moon as part of a great national effort of the United States of America. Many years ago, the great British explorer George Mallory, who was to die on Mount Everest, was asked why did he want to climb it? He said, “Because it is there.” Well, space is there, and we’re going to climb it, and the moon and the planets are there, and new hopes for knowledge and peace are there. And, therefore, as we set sail we ask God’s blessing on the most hazardous and dangerous and greatest adventure on which man has ever embarked. Thank you."
import re
jfk_words = re.split(r"[\W]+", jfk.lower())
jfk_words = [w for w in jfk_words if w != ""]

print(len(jfk_words))        # tokens
print(len(set(jfk_words)))   # types

jfk_counts = {}

for w in jfk_words:
    if w in jfk_counts:
        jfk_counts[w] += 1
    else:
        jfk_counts[w] = 1

print(jfk_counts)

print("====Nested Loops====")
languages = ["Hittite", "Sanskrit", "Latin", "Gothic", "Tocharian"]
dates     = [-1650, -1200, -700, 350, 600]

attested_lang = {}

for i in range(len(languages)):
    attested_lang[languages[i]] = dates[i]

print(attested_lang)

#same thing, but shorter:
attested_lang2 = {}

for lang, date in zip(languages, dates):
    attested_lang2[lang] = date

print(attested_lang2)

languages = ["Hittite", "Sanskrit", "Latin", "Gothic", "Tocharian"]
dates     = [-1650, -1200, -700, 350, 600]
branch    = ["Anatolian", "Indo-Iranian", "Italic", "Germanic", "Tocharian"]

lang_info = {}

for lang, date, br in zip(languages, dates, branch):
    lang_info[lang] = [date, br]

print(lang_info)

print("====Activity====")
consonant =  ["p", "b", "t", "d", "k", "g", "s", "z", "m", "n", "l", "r", "w", "j", "h"]
place = ["bilabial", "bilabial", "alveolar", "alveolar", "velar", "velar", "alveolar", "alveolar", "bilabial", "alveolar", "alveolar", "alveolar", "labial-velar", "palatal", "glottal"]
manner = ["stop", "stop", "stop", "stop", "stop", "stop", "fricative", "fricative", "nasal", "nasal", "lateral", "trill", "glide", "glide", "fricative"]
voice = ["voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiceless"]

phon_info = {}
for phon, place, manner, voice in zip(consonant, place, manner, voice):
    phon_info[phon] = [place, manner, voice]

print(phon_info)

print("Z =", phon_info['z'])
print("Z's manner = ", phon_info['z'][1])

for phon in phon_info:
    if phon_info[phon][1] == "stop" and phon_info[phon][2] == "voiced":
        print(phon)

print("====Nested Loops====")
words = ["eeny", "meeny", "miney", "mo"]
vowel_counts = {}

for w in words:
    vowels = 0                 # reset the counter for each word
    for c in w:
        if c in "aeiou":
            vowels += 1
    vowel_counts[w] = vowels

print(vowel_counts)

print("====Activitity====")
words = [
    ["lin", "guis", "tics"],
    ["pho", "no", "lo", "gy"],
    ["mor", "pho", "lo", "gy"],
    ["se", "man", "tics"]
]

#1
for word in words:
    for syll in word:
        print(syll)

#2
total_syllies = 0
for word in words:
    for syll in word:
        total_syllies += 1

print(total_syllies)

#3
for word in words:
    print(word, len(word))

#4
pho_count = 0
for word in words:
    for syll in word:
        if syll == "pho":
            pho_count += 1
print(pho_count)