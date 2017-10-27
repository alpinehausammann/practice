import re
def is_isogram(string):
    if string != "":
        string = re.findall(r'[^-_. ]', string.lower())
        used_letters = []
        for letter in string:
            if letter in used_letters:
                return False
            else:
                used_letters.append(letter)
                if len(string) == len(used_letters):
                    return True
    else:
        return True