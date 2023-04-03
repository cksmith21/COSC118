# Project Two - COSC118
# Caroline Smith
# 3 April 2023

# function to draw the rectangle
def rect(length, width):
    
    # print the rectangle
    print()
    for i in range(length):
        print("*"*width)
    print()

# function to draw the right triangle
def right_isosceles(levels):
    
    # draw the upper half of the triangle
    print()
    for i in range(1,levels, 1):
        print("*"*i)

    # draw the bottom half of the triangle
    for i in range(levels, 0, -1):
        print("*"*i)
    print()

# function to draw the left triangle
def left_isosceles(levels):

    # draw the upper half
    print()
    for i in range(1, levels+1):
        print(' '*(levels-i) + '*'*i)

    for i in range(levels, 1, -1):
        print(' '*(levels+1-i) + '*'*(i-1))
    print()

# function to draw the up triangle
def up_isosceles(levels):
    
    # draw the whole triangle
    print()
    for i in range(levels+1):
        spaces = levels-i
        print (' '*spaces + '*'*i + '*'*(i-1))
    print()

# function to draw the down facing triangle
def down_isosceles(levels):

    spaces = 0

    # draws the whole triangle
    print()
    for i in range(levels, 0, -1):
        print(' '*spaces, "*"*((i*2)-1))
        spaces += 1
    print()


if __name__ == "__main__":

    print("Indicate whether you want to: ")
    print("1. Draw a rectangle.")
    print("2. Draw an isosceles triangle. ")

    choice = int(input("Select a number or 0 to exit: "))

    while choice != 0:

        if choice == 1:

            width = int(input("How wide should the rectangle be? "))
            length = int(input("How tall should the rectangle be? "))
            rect(length, width)
        
        elif choice == 2: 

            levels = int(input("Enter an odd number for number of levels: "))
            while levels % 2 == 0: 
                levels = int(input("Enter an odd number for number of levels: "))

            print("What direction would you like the triangle to point? ")
            print("1. down \n2. up\n3. left \n4. right")
            direction = int(input("Select a number: "))

            if direction == 1:
                down_isosceles(levels)
            elif direction == 2:
                up_isosceles(levels)
            elif direction == 3:
                left_isosceles(levels)
            elif direction == 4:
                right_isosceles(levels)
            else:
                print("Invalid number.")
                break
        else: 

            print("Invalid choice.")
            break 

        print("Indicate whether you want to: ")
        print("1. Draw a rectangle.")
        print("2. Draw an isosceles triangle. ")

        choice = int(input("Select a number or 0 to exit: "))