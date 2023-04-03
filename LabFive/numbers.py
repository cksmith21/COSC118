if __name__ == "__main__":

    nums = []
    for i in range(0, 20):
        nums.append(int(input("Enter a number: ")))

    print(f'The lowest number: {min(nums)}.')
    print(f'The highest number: {max(nums)}.')
    print(f'The total numbers in the list: {sum(nums)}.')

    avg = sum(nums)/float(len(nums))

    print(f'The average of the numbers in the list: {avg}.')