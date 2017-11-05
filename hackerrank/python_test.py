##Breaks words into two strings that are elements of even and odd indexes respectively

class Seperator:
    def __init__(self):
        self.num = 0
        self.strings = []
    
    def words(self):
        if 0 <= self.num <= 10 and 2 <= len(self.strings) <= 10000:

            for i in range(self.num):
                even = ""
                odd = ""
                for index, letter in enumerate(self.strings[i]):
                    if index % 2 == 0:
                        even += letter
                    else:
                        odd += letter
                print("{} {}".format(even, odd))
        else:
            pass

    def u_input(self):
        self.num = int(input())
        for i in range(self.num):
            self.strings.append(str(input()))
        return self.num, self.strings

a = Seperator()
a.u_input()
a.words()