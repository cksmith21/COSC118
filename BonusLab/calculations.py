if __name__ == "__main__":

    my_dict = {'A':25, 'B':30, 'C':24, 'D':10, 'E':5, 'F':90, 'G':11, 'H':0.56, 'I':3.14}

    max=0
    for key in my_dict:
        if my_dict[key] > max:
            max = my_dict[key]

    print(f'The max is: {max}.')

    min = max
    for key in my_dict:
        if my_dict[key] < min:
            min = my_dict[key]
    
    print(f'The min value is: {min}.')

    sum = 0
    for key in my_dict:
        sum += my_dict[key]

    print(f'The sum is: {sum}.')
    print(f'The average of all of the values is: {sum/len(my_dict):.2f}.')