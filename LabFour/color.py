if __name__ == "__main__": 

    color1 = input("Enter 'red', 'blue', or 'yellow': ")
    color2 = input("Enter a different color from the first (red, blue, or yellow): ")

    colors = ['red', 'blue', 'yellow']

    if color1 not in colors or color2 not in colors:
        print("Color 1 or color 2 is invalid.")
    elif color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
        print("Orange")
    elif color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red':
        print("Purple")
    elif color1 == 'yellow' and color2 == 'blue' or color1 == 'blue' and color2 == 'yellow':
        print("Green.")
    else: 
        print("Color 1 and color 2 are the same.")