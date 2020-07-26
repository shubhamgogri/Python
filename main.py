import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def get_word(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        x = input("Did u mean %s instead? press Y if yes else press N" % get_close_matches(w, data.keys())[0])
        x = x.lower()
        if x == "y":
            correct = get_close_matches(w, data.keys())[0]
            return data[correct]
        elif x == "n":
            return "The Word Doesn't exists."
        else:
            return "We did npt understood the input"
    else:
        return "Please check the word again."


word = input("Enter a word: ")
final = get_word(word)

if type(final) == list:
    for items in final:
        print(items)
else:
    print(final)
