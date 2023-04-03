if __name__ == "__main__": 

    starting_weight = int(input("Enter your starting weight: ")) 
    weights = [starting_weight-(i*4) for i in range(0, 7)]

    for i in range(len(weights)):
        print(f'Weight after {i} months: {weights[i]} pounds.')
        print('-'*30)