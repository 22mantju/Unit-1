#!/usr/bin/env python3
# Valeriy Zagidulin
# 12/4/19
# Wizard Inventory

import os

#displays the menu
def display_menu():
    print("The Wizard Inventory program\n")
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program\n")

#displays the list
def show_list(item_list):
    if len(item_list) == 0:
        print("There are no items to show.\n")
        return
    else:
        i = 1
        for items in item_list:
            row = items
            #print(item)
            print(str(i) + ". " + row[0])
            i += 1
        print()
    return

#adds a item to the list but not exceeding 4
def grab_list(item_list):
    while len(item_list) < 4:
        name_item = input("Name: ")
        item = []
        item.append(name_item)
        item_list.append(item)
        print(item[0], "was added.\n")
        return

    if len(item_list) >= 4:
        print("You can't carry any more items. Drop something first.\n")

#function to edit list
def edit_list(item_list):
    item_in_list = int(input("Number: "))
    if item_in_list <= len(item_list) and item_in_list > 0:
        item_in_list -= 1
        updated_item = str(input("Updated name: "))
        item_list[item_in_list][0] = updated_item
        item_in_list = item_in_list + 1
        print("Item number " + str(item_in_list) + " was updated\n")

    elif item_in_list > len(item_list) or item_in_list < 1:
        print("the number you entered is invalid.\n")
    return

#function to drop item
def drop_list(item_list):
        number = int(input("Number: "))
        #validate the input 
        if number <= len(item_list) and number > 0:
            item_dropped = str(item_list[number - 1][0])
            item_list.pop(number - 1)
            print(item_dropped + " was dropped.\n")

        elif number > len(item_list)  or number < 1:
            print("the number you entered is invalid.\n")

#clears the terminal
def clear_terminal():
    os.system('clear||cls')
    display_menu()        

#main function
def main():
    #clears the terminals 
    os.system('clear||cls')

    #it's the item list
    item_list = [["wooden staff"],
                ["wizard hat"],
                ["cloth shoes"]]

    #calls display_menu function
    display_menu()
    while True:        
        command = input("Command: ").lower()
        if command == "show":
            show_list(item_list)

        elif command == "grab":
                grab_list(item_list)

        elif command == "edit":
            edit_list(item_list)

        elif command == "drop":
            drop_list(item_list)

        elif command == "clear":
            clear_terminal()

        elif command == "exit":
            break

        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()