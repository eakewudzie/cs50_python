#this is a kitchen inventory tracker that allows the user to add, remove, and view items in their kitchen inventory. 
# It also allows the user to check if an item is in stock and to update the quantity of an item. 

available_eggs = 1
available_flour = 2
available_sugar = 3



def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

check_kitchen_stock()

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

use_eggs(9,2)
print(available_eggs) # 1. The value of available_eggs is not updated because the function does not modify the global variable. It only returns a new value.

use_eggs(available_eggs, 1)
print(available_eggs)

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1# checks if there is at least 1 egg available to make a fried egg. It returns True if there are enough eggs, and False otherwise.

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs

available_eggs = make_fried_egg(available_eggs) 
# this updates the value of available_eggs with the new value returned by the make_fried_egg function. 
#It ensures that the global variable reflects the current state of the kitchen inventory after making a fried egg.    

check_kitchen_stock() #calls the check_kitchen_stock function to display the updated kitchen inventory after making a fried egg.