if __name__ == "__main__":
    
    pockets = ["green"] + ["red" if i%2 == 1 else "black" for i in range(1,11)] + \
        ["black" if i%2==1 else "red" for i in range(11,19)] + \
        ["red" if i%2 == 1 else "black" for i in range(19,29)] + \
        ["black" if i%2==1 else "red" for i in range(29,36)]
    
    user_input = int(input("Enter a pocket number: "))

    if user_input > 36 or user_input < 0: 
        print("Error. Invalid number.")
    else:
        print(f"The pocket {user_input} is {pockets[user_input]}.")