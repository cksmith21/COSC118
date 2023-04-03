def leagues_to_feet(leagues):
    return leagues*18228.3

if __name__ == "__main__":

    leaguesIn = float(input("Enter the number of leagues: "))
    feetOut = leagues_to_feet(leaguesIn)

    print(f'There are feet {float(feetOut):.2f} in {leaguesIn:.2f} leagues')