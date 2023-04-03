if __name__ == "__main__": 

    one = float(input("Please enter a number: "))
    two = float(input("Please enter a number: "))
    three = float(input("Please enter a number: "))
    four = float(input("Please enter a number: "))
    five = float(input("Please enter a number: "))

    print(f'The minimum value: {min(one, two, three, four, five)}.')
    print(f'The maximum value: {max(one, two, three, four, five)}.')
    print(f'The rounded values are: {round(one, 2)}, {round(two, 2)}, {round(three, 2)}, {round(four, 2)}, {round(five, 2)}.')