def area(sideLength): 
    return sideLength**2

if __name__ == '__main__':

    sideOne = float(input("Enter the side length of the first square: "))
    sideTwo = float(input("Enter the side length of the second square: "))

    areaOne = area(sideOne)
    areaTwo = area(sideTwo)

    print(f'The difference between the areas of squares one and two is: {areaOne-areaTwo:.2f}.')