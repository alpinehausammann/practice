import re
def word_count(phrase):
    word_dict = {}

    for word in re.findall(r'[0-9a-zA-Z]+[\']?[0-9a-zA-Z]+', phrase.lower()):
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    for word in re.findall(r'[0-9]+', phrase.lower()):
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            continue
    return word_dict
    print(word_dict.items())


word_count("hi there jimmy there hi they")
