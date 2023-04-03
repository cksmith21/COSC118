if __name__ == "__main__": 

    day = int(input("Please enter the day of the week as a number (1 = Monday, etc.): "))

    if day == 1:
        print("Monday")
    elif day == 2: 
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("Invalid day, range is 1 thru 7.")