phoneBook = {}
tries = 3
while True:
    try:
        n = int(input())
    except ValueError:
        tries -= 1
        if tries == 0:
            print("You have reach the maximum amount of invalid entries\nAborting.")
            break
        else:
            print("Entry was not an integer, please try again.")
            continue

    for i in range(n):

        while True:
            try:
                name, number = input().strip().split()
            except ValueError:
                break

            if len(number) != 8:
                break
            else:
                phoneBook[name] = number
                break

    for i in range(10**5):
        name = str(input().strip())
        try:
            phoneBook[name]
        except KeyError:
            if name != "":
                print("Not Found")
                pass
            else:
                break
        else:

            print("{}={}".format(name, phoneBook[name]))
    break
