# project on cafe menu and billing
menu = {
    'tea': 30,
    'coffe': 50,
    'pasta': 60,
    'sandwich': 50,
    'roll':70
}
print("welcome to Krishna cafe")
print("MENU\nTea Rs30\nCoffe RS50\nPasta Rs60\nSandwich Rs50\nRoll Rs70")
item_1 =input("please enter your order ")
order_total =0
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your order {item_1}s confirmed")
else:
    print("please enter item present in menu.")
another_order = input("would you like to order something more(yes/no) ")
if another_order== "yes":
    item_2 = input("please enter next your order ")
if item_2 in menu:
    order_total +=menu[item_2]
    print(f"your order {item_2} confirmed")
    print("your to total bill= Rs",order_total)
else:
    print("please enter item present in menu. Thanku!")

print("Thanku for visiting us. please visit again!\nHAve a nice day")
