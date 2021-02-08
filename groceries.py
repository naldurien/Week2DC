# Week 2 Day 1 Assignment - Grocery App

import sys
store_list = []

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.item_list = []

    #def get_name(self, name):
     #   return self.name

    #def __str__(self):
     #   return str(self.name)


class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

   #def __str__(self):
    #    return f"{str(self.name)}, qty: {str(self.qty)}"

    #def get_name(self, name):
     #   return self.name

    #def get_qty(self, qty):
     #   return self.qty

      
while True:
    selection = input("""
    Press 1 to add a store.
    Press 2 to add items to a store's list.
    Press 3 to view all current lists.
    Press q to quit.
    Enter your selection: """)


# 1: Create a Store object and add it to a list:
    if selection == "1":
        store = input("Enter a store name: ")
        address = input("Enter store address: ")
        if store not in store_list:
            create_store = Store(store, address)
            store_list.append(create_store)
        counter = 1
        for i in store_list:
            print(f"{counter} - {i.name}, located at {i.address}")
            counter +=1


# 2: View store list, let user select a store and add an item, create an Item object and append to store's self.items list]
    if selection == "2":
        counter = 1
        print("Current List of Stores:")
        for i in store_list:
            print(f"{counter} - {i.name}, located at {i.address}")
            counter +=1
        store_select = int(input("Select a store by number: "))
        item = input("Enter an item name: ")
        price = input("Enter the item's price: ")
        qty = input("Enter desired quantity: ")
        create_item = Item(item, price, qty)
        store_list[store_select-1].item_list.append(create_item)
        print(f"{create_item.name}, Price: ${create_item.price}, Qty: {create_item.qty}")
        #print(store_list[store_select-1].items[0])
 
 # 3: View all lists for all stores simultaneously.
    if selection == "3":
        print("\n- - - MASTER LIST - - -")
        counter = 1
        for i in store_list:
            print(f"{counter} - {i.name}, located at {i.address}")
            counter +=1
            for j in i.item_list:
                print(f"{j.name} - ${j.price} - Qty: {j.qty}")
        
 #4: Allow user to exit.          
    if selection == "q":
        quit()
