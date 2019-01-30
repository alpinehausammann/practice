# Score categories
# Change the values as you see fit
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"
NUMBER_CATEGORIES = {"ones": 1, "twos": 2,
                     "threes": 3, "fours": 4, "fives": 5, "sixes": 6}


def number_sort(arr):
    temp_arr = []

    for item in arr:
        if item not in temp_arr:
            temp_arr.append(item)

    return temp_arr


def number_count(arr, comp_arr):
    temp_arr = []

    for i in comp_arr:
        counter = 0
        for j in arr:
            if i == j:
                counter += 1
        temp_arr.append((i, counter))

    return temp_arr


def full_house(arr):
    arr = number_count(arr, number_sort(arr))
    three = False
    two = False

    if len(arr) != 2:
        return 0
    for i in arr:
        if i[1] == 2:
            two = True
        elif i[1] == 3:
            three = True
    if two == True and three == True:
        return (arr[0][0] * arr[0][1]) + (arr[1][0] * arr[1][1])
    else:
        return 0


def choice(arr):
    total = 0
    for i in arr:
        total += i
    return total


def straight(arr, size):
    little = [1, 2, 3, 4, 5]
    big = [2, 3, 4, 5, 6]
    arr = number_sort(arr)
    if len(arr) != 5:
        return 0
    else:
        if size.lower() == "little":
            if bool(set(little).difference(arr)):
                return 0
            return 30

        if size.lower() == "big":
            if bool(set(big).difference(arr)):
                return 0
            return 30


def yacht(arr):
    arr = number_count(arr, number_sort(arr))
    if len(arr) != 1:
        return 0
    else:
        if arr[0][1] != 5:
            return 0
        return 50


def sum_of_numbers(arr, num):
    arr = number_count(arr, number_sort(arr))
    for i in arr:
        if i[0] == num:
            return num * i[1]
    return 0


def four_of_a_kind(arr):
    arr = number_count(arr, number_sort(arr))
    for i in arr:
        if i[1] >= 4:
            return i[0] * 4
        return 0


def score(arr, category):
    category = category.lower()

    if category == "yacht":
        return yacht(arr)
    elif category == "full_house":
        return full_house(arr)
    elif category == "four_of_a_kind":
        return four_of_a_kind(arr)
    elif category == "choice":
        return choice(arr)
    elif category == "big_straight":
        return straight(arr, "big")
    elif category == "little_straight":
        return straight(arr, "little")
    elif category in NUMBER_CATEGORIES.keys():
        return sum_of_numbers(arr, NUMBER_CATEGORIES[category])
    else:
        return 0
