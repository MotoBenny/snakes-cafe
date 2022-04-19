"""
Lab: Class 1 - Intro to Python
Overview
Today you’ll begin working on a command line utility which will mimic the functionality of a point
of sale restaurant system using your basic Python tools and understanding of the basics of the language.
"""
import sys

"""
Build a restaurant point of sale/order system
Feature Tasks and Requirements
* When run, the program should print an intro message and the menu for the restaurant
* The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
* The program should prompt the user for an order
* When a user enters an item, the program should print an acknowledgment of their input
* The program should tell the user how to exit
* The program’s content should match included sample exactly
    * Actually, there’s one tiny spot that should be different - see if you can spot it.
    * The > character represents user input line and should be printed out with a trailing space.

pseudo code:
1) create functions for the different functionality you need.
2) build logical control flow that calls the functions as needed.
3) could build this as a while loop with while true, < would prefer to find another method of handing this flow

"""
appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']
menu_items = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon',
              'Steak', 'Meat Tornado', 'A Literal Garden',
              'Ice Cream', 'Cake', 'Pie',
              'Coffee', 'Tea', 'Unicorn Tears']


def display_menu_items(menu_list):
    # pass any of the above lists into display_menu_items
    # to print that menu section to screen.
    for item in menu_list:
        print(item)
    print("\n")


def handle_order():  # this needs logic to check the order_list for repeats and display the number.
    user_order = input('> ').capitalize()
    if user_order in menu_items:
        return user_order
    elif user_order == 'Quit':
        return user_order
    else:
        print("That item is not on the menu, please order from the menu")
        handle_order()


def exit_snakes_cafe():
    print("Thank you for visiting Snakes Cafe (Powered by AWS)")
    sys.exit()  # this will close the script.


def snakes_cafe():
    """meat of the application, will handle the control flow for the snake_cafe.
        research ways to build this control flow without using a while statement."""
    order_dict = {}
    while True:
        order = handle_order()
        if order == 'Quit':
            exit_snakes_cafe()
        elif order not in order_dict:
            order_dict[order] = 1
            print(f"""** 1 order of {order} has been added to your meal **""")
        else:
            order_dict[order] += 1
            if order_dict[order] > 1:
                print(f"""** 1 order of {order} has been added to your meal, 
Your order now contains {order_dict[order]} orders of {order} **""")


# refactor this to use the display menu items func
greeting = "\n".join((
    "**************************************",
    "**    Welcome to the Snakes Cafe!   **",
    "**    Please see our menu below.    **",
    "**                                  **",
    '** To quit at any time, type "quit" **',
    "**************************************",
    "\n"
))
menu_apps = "\n".join((
    "Appetizers",
    "----------",
))
menu_entrees = "\n".join((
    "Entrees",
    "-------",
))
menu_desserts = "\n".join((
    "Desserts",
    "--------",
))
menu_drinks = "\n".join((
    "drinks",
    "------",
))
order_print = "\n".join((
    "***********************************",
    "** What would you like to order? **",
    "***********************************",
))

print(greeting)
print(menu_apps)
display_menu_items(appetizers)
print(menu_entrees)
display_menu_items(entrees)
print(menu_desserts)
display_menu_items(desserts)
print(menu_drinks)
display_menu_items(drinks)
print(order_print)
snakes_cafe()
