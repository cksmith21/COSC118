def get_avg(elements):
    return(sum(elements)/len(elements))

def get_smaller_count(elements, avg):
    count=0
    for el in elements:
        if el < avg:
            count+=1
    return count

if __name__ == "__main__":

    numbers = [int(input("Enter number: ")) for i in range(8)]
    avg = get_avg(numbers)
    print(f'The number of values less than the average ({avg}) is {get_smaller_count(numbers, avg)}.')