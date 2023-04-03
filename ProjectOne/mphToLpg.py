def MPGtoLP100km(milespergallon):
    return 235.21/milespergallon

if __name__ == "__main__": 

    mpg = float(input("How many miles per gallon? "))
    lp100km = MPGtoLP100km(mpg)

    print(f'{mpg:.2f} mpg is equivalent to {lp100km:.2f} liters per 100km.')