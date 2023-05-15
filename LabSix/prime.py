def is_prime(val):

    if val == 0 or val == 1:
        return False
    
    for i in range(2,val):
        if val % i == 0:
            return False
    
    return True

if __name__ == "__main__":

    value = int(input("Enter a value to check if it is prime: "))

    if is_prime(value):
        print("The number is prime.")
    else:
        print("The number is not prime.")