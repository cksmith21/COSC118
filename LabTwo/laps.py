def laps(target, length):

    low = target//length
    high = low + 1

    print(f'You must run between {low} and {high} laps.')

if __name__ == "__main__":

    targetLength = float(input("How many miles would you like to run? "))
    trackLength = float(input("How long is the track in miles? "))

    laps(targetLength, trackLength)
