#!/usr/bin/python
# amazon_account.py

'''creates class called AmazonAccount that has account related modules'''

__author__ = "Gregory Chekler"
__version__ = "1.0"


class AmazonAccount:
    def __init__(self, name, email_address, password, gift_balance=0):
        """constructor

        :param name: user's name
        :param email_address: user's email adress
        :param password: user's password
        :param gift_balance: user's gift balance
        """
        self.name          = name
        self.email_address = email_address
        self.password      = password
        self.gift_balance  = gift_balance
        self.purchases     = []


    def add_gift_amt(self, gift_amt):
        """adds money to gift amount

        :param gift_amt: the amount of money that user wants to add
        :return: updated gift amount
        """
        self.gift_balance += gift_amt

    def change_email(self, email_1, email_2):
        """changes the users email

        :param email_1: first email input
        :param email_2: second email input
        :return: changed email address
        """
        while (email_1 != self.email_address) or (email_2 != self.email_address):
            print("Incorrect. Please input the email address twice again.")
            email_1 = input("Input email address: ")
            email_2 = input("Input email address again: ")

        if (email_1 == self.email_address) and (email_2 == self.email_address):
            new = input("Input new email address: ")
            self.email_address = new
            print("You have changed your email address.")


    def show_info(self):
        """shows all of the data about user

        :return: all user data
        """
        print("The name is: ",         self.name)
        print("The email is: ",        self.email_address)
        print("The password is",       self.password)
        print("The gift balance is: ", self.gift_balance, "dollars")
        print("The purchases are: ",   self.purchases, "\n")#\n makes sure that there is space between accounts

    def purchase_item(self, item):
        """allows user to purchase item and/or checks availability

        :param item: purchases item ro says it is not available
        :return:
        """
        if item.available == True: #implemented for phase 3
            if self.gift_balance >= item.price:
                item.available = False
                self.purchases.append(item.name)
                self.gift_balance -= item.price
        else:
            print("Item is not available\n")

class Item:
    def __init__(self, name, price, category, available=True):
        """constructor for item

        :param name: item's name
        :param price: item's price
        :param category: item's category
        :param available: items's availability
        """

        self.name = name
        self.price = price
        self.category = category
        self.available = available

    def show_info(self):
        """shows all of the data about item

        :return: all item data
        """
        print("The item is: ",     self.name)
        print("The price is: ",    self.price, "dollars")
        print("The category is: ", self.category)
        print("It is available: ", self.available, "\n")#\n makes sure that there is space between items

