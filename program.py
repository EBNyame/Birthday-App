# the birthday app

import datetime

def header():
    print("-------------------------------------------------------------")
    print("                       BIRTHDAY APP                          ")
    print("-------------------------------------------------------------")
    print()


def get_birthday_date_from_user():
    print("Tell us when you were born")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds()/60/60/24)
    return days


def print_birthday_information(days):
    if days < 0:
        print("your birthday is in {} days!".format(-days))
    elif days > 0:
        print("you had your birthday already this year! {} days ago".format(days))
    else:
        print("Happy Birthday!!!")


def main():
    header()
    bday = get_birthday_date_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)





main()