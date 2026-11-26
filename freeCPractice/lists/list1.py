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




#list methods
#append() method adds an item to the end of a list
#pop() method removes and returns the last item from a list
#sort() method sorts the items in a list in ascending order
numset1 = [5, 2, 9, 1, 7]
numset1.append(4)
print(numset1) 

namesOfPeople = ['Alice', 'Bob', 'Charlie']

numset1.append(namesOfPeople) #appended this list to numset1
print(numset1) 

#extend() method adds all the items from an iterable (like a list) to the end of the list
odd_numbers = [1, 3, 5]
even_numbers = [2, 4, 6]
all_numbers = []
all_numbers.extend(odd_numbers)
all_numbers.extend(even_numbers)


print(all_numbers) 

all_numbers.insert(2,10) #inserts 10 at index 2
print(all_numbers)

all_numbers.remove(3) #removes the first occurrence of 3 from the list
print(all_numbers)

#pop() method removes and returns the last item from a list
#pop() with an index removes and returns the item at that index

all_numbers.pop()
print(all_numbers)
all_numbers.pop(2) #removes the item at index 2
print(all_numbers)


#clearing a list
all_numbers.clear()
print(all_numbers)

#sort() method sorts the items in a list in ascending order
numbers = [19, 2, 35, 1, 67, 41 ,500 ,0.2, 3]
numbers.sort()
print(numbers)

#sorted() function returns a new sorted list from the items in an iterable
#this maintains the original list unchanged
numbers1 = [19, 2, 35, 1, 67, 41 ,500 ,0.2 ,3]
sorted_numbers1 = sorted(numbers1)
print(numbers1)  
print(sorted_numbers1)

#reverse() method reverses the order of items in a list
numbers2 = [1, 2, 3, 4, 5]
numbers2.reverse()
print(numbers2)

list_of_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
list_of_names.index('Charlie') # returns the index of the first occurrence of 'Charlie' in the list
print(list_of_names.index('Charlie'))