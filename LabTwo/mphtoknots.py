def mph_to_knots(mph):
    return mph * 0.868976

if __name__ == "__main__":

    mph = float(input("Enter the speed in miles per hour: "))
    knots = mph_to_knots(mph)

    print(f'{mph:.2f} MPH is equivalent to {float(knots):.2f} knots')