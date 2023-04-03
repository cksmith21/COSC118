if __name__ == "__main__":

    miles = input("Enter the miles driven: ")
    gas = input("Enter the gallons of gas used: ")

    mpg = float(miles)/float(gas)

    print("MPG: " + f'{mpg:.2f}')
