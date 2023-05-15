def is_prime(val):
    
    if val == 0 or val == 1:
        return False

    for i in range(2,val):
        if val % i == 0:
            return False
    
    return True

if __name__ == "__main__":

    primes = [] 

    for i in range(1, 101): 
        if i == 1:
            pass
        elif is_prime(i):
            primes.append(i)
    
    print(*primes)