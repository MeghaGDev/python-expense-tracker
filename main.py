""" expense = {
    "name": "Lunch",
    "amount": 150,
    "category": "Food"
} """

expenses = []


while True:
    print('\n--------Expense Tracker-------')
    print('1. Add Expense')
    print('2. View all expense')
    print('3. Show total spending')
    print('4. Filter expense by category')
    print('5. delete an expense')
    print('6. Exit')



    choice = input('Enter your choice:')


    #add expense 
    if choice == "1":
        name = input("Enter the expense name: ")
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")

       

        expense ={
            "name":name,
            "amount":amount,
            "category":category
        }

        expenses.append(expense)

        print(f"{name} Successfully Added!")
        print(expense)

    elif choice == "2":

        if not expenses:
            print("no expense found !")
        else:
            for item in expenses:
                print("Name:", item["name"])
                print("Amount:", item["amount"])
                print("Category:", item["category"])
                print("----------------------")

    elif choice == "3" :
        if not expenses :
            print('no expense found !')
        else : 
            count = 0
            for item in expenses:
                count += item["amount"]
            

            print(f"{count}  is total spending")

    elif choice == "4":
        cat = input('Enter the category to check :')
        
        for item in expenses: 
            if(item['category'] == cat):
                print(item)

            else:
                print("No expenses found for this category!")

    elif choice == "5":
        if not expenses:
            print("No expenses found!")
        else:
            name = input("Enter expense name to delete: ")

            found = False

            for item in expenses:
                if item["name"].lower() == name.lower():
                    expenses.remove(item)
                    print(f"{name} deleted successfully!")
                    found = True
                    break

            if not found:
                print("Expense not found!")


    elif choice == "6":
        print("existing")
        break


    else:
        print('In-valid choice')