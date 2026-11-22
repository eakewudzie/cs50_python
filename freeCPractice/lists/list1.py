cities = ['Los Angeles', 'London', 'Tokyo']
cities[0]
print(cities[0]) # Los Angeles


#list constructor ---- coverts an iterable into a list
best_developer = 'Eunice'
my_list = list(best_developer)
print(my_list) 

#length of a list
print(len(my_list)) 



#updating a list
print(cities) # ['Los Angeles', 'London', 'Tokyo']  
cities[0] = 'New York'
print(cities) 


#removing an item from a list using the del statement
del cities[1]
print(cities) # ['New York', 'Tokyo']


#checking if an item is in a list
programming_languages = ['Python', 'Java', 'C++', 'Rust']

print('Rust' in programming_languages) # True
print('JavaScript' in programming_languages)     # False


#Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0])
print(nested_list[0][1]) # 2
print(nested_list[2][2]) 

#unpacking values from a list 
#assigning values from a list to variables

devNames = ['Eunice', 'John', 'Mary']
name1, name2, name3 = devNames
print(name1)
print(name2)
print(name3)

SmithInfo = ['John', 'Smith', 30, 'Engineer']
first_name, *rest = SmithInfo
print(first_name) 
print(rest) # ['Smith', 30, 'Engineer']  the *rest variable collects all the remaining values from the list into a new list.    

#slicing a list
numbers = [100, 200, 300, 400, 500]
print(numbers[1:4])
print(numbers[1::2]) # [200, 400]  the slice starts at index 1, taking every second element.
