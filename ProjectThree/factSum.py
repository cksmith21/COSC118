if __name__ == "__main__": 

    user_input =int(input("Enter a value greater 0: "))
    while(user_input <= 0):
        user_input = int(input("Enter a value greater 0: "))

    sum = sum([i for i in range(user_input+1)])
    fact = 1
    for i in range(1,user_input+1):
        fact *= i 

    print(f'The difference between the factorial and sum is {fact - sum}.')