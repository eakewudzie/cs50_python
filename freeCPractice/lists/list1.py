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