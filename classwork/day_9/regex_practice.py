import re                                                     

with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:  
    text = f.read()                                      
matches = re.findall(r"c.t", text)                              # reads the whole file into one string, called `text`