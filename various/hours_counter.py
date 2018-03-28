
hours_total = 0
minutes_total = 0

def add_hours(hours, hours_total, minutes_total):

    for i in hours:
        seperator = i.find(":")
        hours_total += int(i[:seperator])
        minutes_total += int(i[seperator + 1:])

    hours_total += minutes_total // 60
    minutes_total = minutes_total % 60

    return hours_total, minutes_total

def output_format(number):

    if len(str(number)) == 2:
        return str(int(number))



if __name__ == "__main__":
    hours = input().strip().split(" ")
    hours_total, minutes_total = add_hours(hours, hours_total, minutes_total)
    print("Total Hours: {}:{}".format(int(hours_total),int(minutes_total)))
