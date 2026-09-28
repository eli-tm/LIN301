x = 50
if x % 2 == 0:
    print(x, "is even")   #tab is required to prevent indentation error

print("============")
y = 51
if y % 2 == 0:
    print(y, "is even")
    print("this command followed through!")
print("if you only see this, y is not even")

print("============")
z = 53
if z % 2 == 0:
    print(z, "is even")
else:
    print(z, "is odd")

print("============")
a = 50.1
x = 50
if a % 2 == 0:
    print(a, "is even.")
elif a % 2 == 1:           #elif is just like if but doesn't occur first
    print(a, "is odd.")
else:
    print(a, "is a decimal.")

print("============")
charlotte = ["The Professor", "Jane Eyre", "Shirley", "Villette"] 
emily = ["Wuthering Heights"] 
anne = ["Agnes Grey", "The Tenant of Wildfell Hall"] 

novel = "Agnes Grey"     # we identify the novel we're looking at
if novel in charlotte: 
    print("Charlotte Brontë wrote", novel)  #we first check to see that our variable is in charlotte
elif novel in emily: 
    print("Emily Brontë wrote", novel) #then emily
elif novel in anne: 
    print("Anne Brontë wrote", novel) #then anne
else: 
    print(novel, "was not written by one of the Brontë sisters") #if the novel is in none of these, we get our else statement

print("============")
bronte_checks = {"charlotte": 0, "emily": 0, "anne" : 0}  #a starter dict, where the values of each bronte book is at 0

if novel in charlotte: 
    bronte_checks["charlotte"] += 1
    print("Charlotte Brontë wrote", novel) 
elif novel in emily: 
    bronte_checks["emily"] += 1
    print("Emily Brontë wrote", novel) 
elif novel in anne: 
    bronte_checks["anne"] += 1
    print("Anne Brontë wrote", novel) 
else: print(novel, "was not written by one of the Brontë sisters")

print(bronte_checks)

print("====== Activity ======")
sound = "y"
vowels = ["a", "e", "i", "o", "u"]
consonants = ["p", "t", "k", "m", "n", "s", "z", "f", "v", "j", "w", "g", "b", "d", "h", "r", "l"]

if sound in vowels:
    print(sound, "is a vowel")
elif sound in consonants:
    print(sound, "is a consonant")
else: print("arfarfarfarfarfarfarf")

sound_checks = {"consonant": 0, "vowel": 0, "puppy": 0}
sound = "y"
if sound in vowels:
    sound_checks["vowel"] += 1
    print(sound, "is a vowel")
elif sound in consonants:
    sound_checks["consonant"] += 1
    print(sound, "is a consonant")
else:
    sound_checks["puppy"] += 1
    print("arfarfarfarfarfarf")

print(sound_checks)
