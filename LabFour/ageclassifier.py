if __name__ == "__main__":

    age = float(input("Please enter your age: "))

    if age < 0: 
        print("Invalid age.")
    elif 0 < age <= 1:
        print("You are an infant.")
    elif 1 < age < 13:
        print("You are a child.")
    elif 13 <= age < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")