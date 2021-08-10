#!/usr/bin/python
# amazon.py

'''creates terminal menu and executes code related to the AmazonAccount and Item classes'''

__author__ = "Gregory Chekler"
__version__ = "1.0"

import amazon_account as aa

#accounts
greg = aa.AmazonAccount("greg", "greg@concordcarlisle.org", "password", 500)
jack = aa.AmazonAccount("jack", "jack@concordcarlisle.org", "password", 200)
sam = aa.AmazonAccount("sam", "sam@concordcarlisle.org", "password")
amazon_customers = [greg, jack, sam]#adds accounts to list

#items
apple = aa.Item("apple", 5, "food")
pear = aa.Item("pear", 2, "food")
keyboard = aa.Item("keyboard", 25, "electronics")
computer = aa.Item("computer", 500, "electronics")
shovel = aa.Item("shovel", 30, "tools")
wrench = aa.Item("wrench", 15, "tools")
Frozen = aa.Item("Frozen", 10, "movies&tv")
friends = aa.Item("friends", 50, "movies&tv")
items = [apple, pear, keyboard, computer, shovel, wrench, Frozen, friends]#adds items to list

run = True #makes while loop run forever
option = 1 #default option
account = greg
item = None

def main():
    """function that contains menu that allows user to use specific methods related to amazon accounts

    :return: runs program and allows user to use methods to preform specific actions
    """

    while run:
        print("Options:\n"
              "1 - Show all accounts\n"
              "2 - Choose an account\n"
              "3 - Add to the gift_balance\n"
              "4 - Purchase an item\n"
              "5 - Change email\n"
              "6 - Add account\n"
              "7 - Show item categories\n" #This is something extra that I implemented for phase 3
              "8 - Quit\n")

        option = int(input("Please input the number correlated to each option "
                           "(if just starting, please choose an account): "))


        if option == 1: #shows all accounts
            for i in range(len(amazon_customers)):
                amazon_customers[i].show_info()

        elif option == 2:#selects account - default is greg
            account = input("Please choose the account you want: ")
            for i in range(len(amazon_customers)): #finds desired account
                if amazon_customers[i].name == account:
                    account = amazon_customers[i]

        elif option == 3:#adds money
            gift = int(input("Please put in the amount of money you want to add to your account: "))
            account.add_gift_amt(gift)

        elif option == 4:#shows items for purchase and then may let you purchase
            print("The items for purchase are:\n")
            for i in range(len(items)):
                items[i].show_info()

            item = input("Please choose the item you want: ")
            for i in range(len(items)): #finds item
                if items[i].name == item:
                    item = items[i]
            account.purchase_item(item)

        elif option == 5:
            account.change_email("", "")#the empty string allows email to be changed without getting error

        elif option == 6: #creates new account
            name = input("Input the name of the new account: ")
            email = input("Input an email address: ")
            password = input("Please input a password: ")
            vars()[name] = aa.AmazonAccount(name, email, password) #dynamically creates a variable
            amazon_customers.append((vars()[name]))

        elif option == 7: #Shows categories of items - I implemented phase 3 a little differently
            print("The items in the food category are: \n")
            for i in range(len(items)):
                if items[i].category == "food":
                    items[i].show_info()

            print("The items in the electronics category are: \n")
            for i in range(len(items)):
                if items[i].category == "electronics":
                    items[i].show_info()

            print("The items in the tools category are: \n")
            for i in range(len(items)):
                if items[i].category == "tools":
                    items[i].show_info()

            print("The items in the movies&tv category are: \n")
            for i in range(len(items)):
                if items[i].category == "movies&tv":
                    items[i].show_info()

        elif option == 8: #quites program
            break

        else:
            pass
main()



