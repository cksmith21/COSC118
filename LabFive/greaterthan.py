from random import randint

def greaterthanN(nums, n):

    print(f"Numbers greater than {n}.")

    for item in nums:
        if item > n:
            print(item, end=' ')
    print('\n')
    
if __name__ == "__main__":

    test_list = [randint(0,100) for i in range (10)]
    n = randint(0, 100)

    greaterthanN(test_list, n)
