import amazon_account as aa

name = aa.AmazonAccount("Greg", "gchekler21@concordcarlisle.org", "password")
apple = aa.Item("Apple", 5)
pear = aa.Item("Pear", 2)
keyboard = aa.Item("Keyboard", 25)
name.add_gift_amt(500)
print(name)
#name.show_info()
#apple.show_info()
name.purchase_item(apple)
name.purchase_item(apple)
#name.change_email("greg@cc", "greg")
name.show_info()
