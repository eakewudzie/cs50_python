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
