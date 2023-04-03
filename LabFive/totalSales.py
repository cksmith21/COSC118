if __name__ == "__main__":

    sales = [] 
    for i in range(7):
        sales.append(int(input(f"Enter the sales for day {i+1} of the week: ")))

    totalSales = 0
    for day in sales:
        totalSales += day

    print(f"The total sales are ${totalSales}.")