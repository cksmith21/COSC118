def volOfCuboid(length, breadth, height):
    return length*breadth*height

if __name__ == "__main__": 

    len = float(input("Enter the length: "))
    bread = float(input("Enter the breadth: "))
    hei = float(input("Enter the height: "))

    volume = volOfCuboid(len, bread, hei)

    print(f'The volume is {volume:.2f} units.')