import re
def word_count(phrase):
    word_dict = {}
    
    for word in re.findall(r'[a-zA-Z][\'a-zA-Z]?', phrase):
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict


word_count("hi there jimmy there hi they")