def add_hours(hours):

    hours_total = 0
    minutes_total = 0

    for i in hours:
        seperator = i.find(":")
        hours_total += int(i[:seperator])
        minutes_total += int(i[seperator + 1:])

    min_to_hours = (minutes_total-(minutes_total%60))/60
    minutes_total = minutes_total%60
    hours_total += min_to_hours

    return hours_total, minutes_total

def output_format(number):

    if len(str(number)) == 2:
        return str(int(number))



if __name__ == "__main__":
    hours = input().strip().split(" ")
    hours_total, minutes_total = add_hours(hours)
    print("Total Hours: {}:{}".format(output_format(hours_total),output_format(minutes_total)))
