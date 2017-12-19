from datetime import datetime, second

def add_gigasecond(birth_date):
    billion = second(10**9)
    birth_date += billion
    return birth_date
