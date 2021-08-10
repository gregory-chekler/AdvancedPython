#!/usr/bin/python
#  many_accounts.py

'''creates many amazon accounts and then displays a random one'''

__author__ = "Gregory Chekler"
__version__ = "1.0"

import random
import amazon_account as aa

amazon_customers = []
def password_generator():
    """Creates a password with one uppercase, five lowercase, one number and one symbol

    :return: returns created password
    """
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*" #string used to create password
    number = random.randint(0,25)# capital letters indices range
    password = string[number]
    for i in range(5):
        number = random.randint(26, 50)# lowercase letters indices range
        password = password + string[number]
    number = random.randint(52, 61)  # number indices in string
    password = password + string[number]
    number = random.randint(62, 69)  # symbol indices in string
    password = password + string[number]

    return password

def main():
    """Main function that creates 100 accounts and then display a random one

    :return: 100 different accounts and prints one random account
    """
    file = open("ALLFirstNames.txt", "r")
    text = file.read()
    list = text.split("\n")
    for i in range(100): #creates accounts
        number = random.randint(0, len(list)-1)
        name = list[number]
        email = name + "@gmail.com"
        password = password_generator()

        #creates amazon account with random name, email, password, and adds gift balance from 0 to 1000 dollars
        vars()[name] = aa.AmazonAccount(name, email, password, random.randint(0, 1000))#dynamically creates a variable
        amazon_customers.append((vars()[name]))

    amazon_customers[random.randint(0, 99)].show_info()#displays random account

    file.close()

'1' = 56
main()

person1 = 50
