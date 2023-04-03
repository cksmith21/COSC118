if __name__ == "__main__":

    month = int(input("Enter the month in integer format: "))
    day = int(input("Enter the day in integer format: "))
    year = int(input("Enter the year as a two digit number: "))

    if month * day == year: 
        print("The date is magic.")
    else: 
        print("The date is not magic")