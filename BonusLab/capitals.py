from random import randint

if __name__ == "__main__": 

    countries = {'South Sudan':'Juba', 'Chad':'NDjamena', 'Bosnia and Herzegovina':'Sarajevo', 'Central African Republic':'Bangui', 'Mali':'Bamako', 'Mozambique':'Maputo', 'Burkina Faso':'Ouagadougou', 'Yemen':'Sanaa', 'Guinea':'Conakry', 'Burundi':'Gitega'}

    num_correct = 0
    num_incorrect = 0
    values_used = []

    keys = list(countries.keys())

    while len(values_used) < 10: 

        rand_value = randint(0,9)

        while rand_value in values_used:
            rand_value = randint(0,9)

        values_used.append(rand_value)

        guess = input(f'What is the capital of {keys[rand_value]}? Please capitalize: ') 

        if guess == countries[keys[rand_value]]:
            print("You are correct!")
            num_correct += 1
        else:
            print(f"You are wrong. It is {countries[keys[rand_value]]}.")
            num_incorrect += 1

    print(f'The total correct is {num_correct} and the total incorrect is {num_incorrect}.')
    