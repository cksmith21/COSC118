if __name__ == "__main__":

    rain = []

    for i in range(12):
        rain_val = float(input(f"Enter the rain for month {i+1}: "))
        rain.append(rain_val)

    print(f'The max amount of rain is: {max(rain)} inches.')
    print(f'The minimum amount of rain is {min(rain)} inches.')
    print(f'The average monthly rainfall is {(sum(rain)/12):.2f} inches.')
    print(f'The total amount of rainfall is {sum(rain):.2f} inches.')