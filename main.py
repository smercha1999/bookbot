def charCounter(stringss):
    charString = [*stringss]
    charString.sort()
    newDict = dict()
    for i in charString:
        if i.lower() not in newDict:
            newDict[i.lower()] = 1
        else:
            newDict[i.lower()] += 1
    for i in newDict:
        if i.isalpha():
            print(f"The {i} character was found {newDict[i]} times")
    return newDict

def wordCount(words):
    wordList = words.split()
    counter = 0
    for i in wordList:
        counter += 1
    print(f"{counter} words found in the document")
    return counter
path = "books/frankenstein.txt"
with open(path) as f:
    file_contents = f.read()
print(f"--- Begin report of {path} ---")
wordCount(file_contents)
charCounter(file_contents)
print("--- End report ---")



