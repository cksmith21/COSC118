from random import randint

if __name__ == "__main__":

    lottery_number = [randint(0,9) for i in range(9)]
    
    for item in lottery_number:
        print(item, end=' ')
    print('\n')