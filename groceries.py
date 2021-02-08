# Week 2 Day 1 Assignment - Grocery App

import sys
store_list = []
main_dict = {} 

class Store:
    def __init__(self, name):
        self.name = name


    def get_name(self, name):
        return self.name


    def __str__(self):
        return str(self.name)




class Item:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty


    def __str__(self):
        return f"{str(self.name)}, qty: {str(self.qty)}"


    def get_name(self, name):
        return self.name


    def get_qty(self, qty):
        return self.qty



        
while True:
    selection = input("""
    Press 1 to add an item.
    Press 2 to view list.
    Press q to quit.
    Enter your selection: """)


    if selection == "1":
        store_select = input("Enter a store name: ")
        item_select = input("Enter an item name: ")
        item_amount = input("Enter desired quantity: ")
        create_item = Item(item_select, item_amount)
        str_item = str(create_item)
        if store_select in store_list:
            for key in main_dict.keys():
                if key == store_select:
                    main_dict[key] += f", {str_item}"
                else:
                    continue
        else:
            if store_select not in store_list:
                store_list.append(store_select)
                create_store = Store(store_select)
                main_dict[str(create_store)] = str_item 
        print(f"Current lists: {main_dict}")


    if selection == "2":           
        print(f"Current lists: {main_dict}") 
    
    
    if selection == "q":
        quit()
