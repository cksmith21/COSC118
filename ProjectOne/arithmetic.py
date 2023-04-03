def expOne(a, b, c):
    return (1/3)*(a*b*c)

def expTwo(n, d):
    return 2*(n/d)

def expThree(e, f):
    return (e+f)**2

if __name__ == "__main__": 

    a = expTwo(28,4)
    temp_b1 = expOne(4, 5, 9)
    temp_b2 = expOne(27, 5, 1)
    b = expThree(temp_b1, temp_b2)
    c = 6

    result = expOne(a, b, c)

    print(f'The result is: {int(result)}.')
