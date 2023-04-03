def ratio(num_cookies): 
    
    sugar = (1.5 / 48) * num_cookies
    butter = (1.0 / 48) * num_cookies
    flour = (2.75 / 48) * num_cookies

    print(f'You will need {sugar:.2f} cups of sugar, {butter:.2f} cups of butter, and {flour:.2f} cups of flour to make {num_cookies} cookies.')

if __name__ == "__main__": 

    cookies = int(input("How many cookies do you want to make? "))
    ratio(cookies)