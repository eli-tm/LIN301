languages = ["Hittite", "Sanskrit", "Latin", "Gothic", "Tocharian"]
dates = [-1650, -1200, -700, 350, 600]
#list method
latin_index = languages.index("Latin") #find position of Latin
print(latin_index)
print(dates[latin_index]) #find Latin date from index
gothic_index = languages.index("Gothic") #do the same for Gothic
print(gothic_index)
print(dates[gothic_index])

#building a dictionary
lang_dict = {
"Hittite": -1650,
"Sanskrit": -1200,
"Latin": -700,
"Gothic": 350,
"Tocharian": 600
}
    #faster way:
attested = {}
for i in range(len(languages)):
    attested[languages[i]] = dates[i]

lang_dict["Latin"]  #look up date for Latin
"Old Irish" in lang_dict  #look for Old Irish in dict
lang_dict["Old Irish"] = 700  #add Old Irish to dict
del lang_dict["Tocharian"]  #delete Tocharian
