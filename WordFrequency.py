specialcharacter = [',','.']

with open('sometext.txt') as text:
    for line in text:
            for x in specialcharacter:
                line=line.replace(x,"")
            words = line.split() 
            uniquewords = dict((word,words.count(word)) for word in set (words))

print(uniquewords)


