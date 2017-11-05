n = int(input())

#phoneBook = {str(key):int(value) for i in range(n) for key, value in [input().strip().split()] if value == 8 }
phoneBook ={}
for i in range(n):
    
    try:
        u_input = input().strip().split()
        if len(u_input[1]) == 8:
            phoneBook[u_input[0]] = int(u_input[1])
        else:
            continue
    except ValueError:
        pass
    print(phoneBook.items())

for i in range(n):
    u_input = str(input().strip())
    try:
        phoneBook[u_input]
    except NameError:
        print("Not Found")
    print("{} = {}".format(u_input, phoneBook[u_input]))