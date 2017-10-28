import re
from string import ascii_lowercase


def is_pangram(sentence):
    
    #compares lowercase ASCII characters a-z 
    #against elements of sentence and creates a list of the difference.
    missing_letters = [x for x in ascii_lowercase if x not in sentence.lower()]

    #If there is any characters in missing_letters, return false
    if len(missing_letters) == 0:
        return True
    else:
        return False
