from random import randint
import math

if __name__ == "__main__": 

    one = randint(10, 26)
    two = randint(10, 26)
    three = randint(10, 26)
    four = randint(10, 26)

    sq_one = math.sqrt(one)
    sq_two = math.sqrt(two)
    sq_three = math.sqrt(three)
    sq_four = math.sqrt(four)

    sum_val = sq_one + sq_two + sq_three + sq_four

    print(f'The sum of the values are: {sum_val:.2f}.')
