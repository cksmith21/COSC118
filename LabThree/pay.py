def cost(charge):

    sales_tax = charge * 0.07
    charge_with_tax = charge + sales_tax
    tip = charge_with_tax * 0.18
    total = charge_with_tax + tip 

    print(f'The cost of the food: ${charge:.2f}.')
    print(f'The sales tax: ${sales_tax:.2f}.')
    print(f'The tip: ${tip:.2f}.')
    print(f'The total cost: ${total:.2f}.')

if __name__ == "__main__":

    cost_of_food = float(input("How much did your food cost? "))
    cost(cost_of_food)

    