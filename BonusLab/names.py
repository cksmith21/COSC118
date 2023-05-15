def menu(): 

    print("Please enter an integer input corresponding to the following menu: ")
    print("0. Exit.")
    print("1. Look up a person's email address.")
    print("2. Add a new name and email address.")
    print("3. Change an existing email address.")
    print("4. Delete an existing name and email address.")
    print()

    val = int(input("Enter your choice: "))
    return val 

if __name__ == "__main__":

    choice = menu() 
    names_and_emails = {} 

    while choice != 0: 

        if choice == 1: 
            name = input("Enter the name you want to look up: ")
            if name not in names_and_emails: 
                print("Name not found.")
            else:
                print(f'The email for {name} is {names_and_emails[name]}.')
        elif choice == 2: 
            name = input("Enter the name: ")
            email = input("Enter the email address: ")
            names_and_emails[name] = email 
        elif choice  == 3:
            name = input("Enter the name to change their address: ")
            if name in names_and_emails:
                email = input("Enter the new email address: ")
                names_and_emails[name] = email
            else:
                print("Name not found.")
        elif choice == 4:
            name = input("Enter the name to delete: ")
            if name in names_and_emails:
                del names_and_emails[name]
            else:
                print("Name not found.")
        else:
            print("Invalid choice.")
        
        choice = menu() 