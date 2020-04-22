#an armstrong number is a number, whom individual digits raised to the length of the number add up to the 
#original number
import math
def armstrong_number(number):
    total = 0
    num_str = str(number)
    for i in range(len(num_str)):
        total += int(num_str[i])**len(num_str)
    return total

print("{}", armstrong_number(123))