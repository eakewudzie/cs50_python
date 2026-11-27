#tuples -- immutable lists. they cannot be changed after they are created.
#tuples are created using parentheses () instead of square brackets [] and can contain mixed data types.
developer = ('Eunice', 30, 'python developer')
print(developer) 

#To create a tuple with one element, you need a trailing comma:
single_value = (5,)
print(single_value) # (5,)

not_a_tuple = (5)
print(not_a_tuple) # 5

empty_tuple = ()
print(empty_tuple) 

#Accessing elements in a tuple is similar to accessing elements in a list, using indexing and slicing.
print(developer[0])
print(developer[-3])



#using the tuple() constructor to create a tuple from an iterable, such as a list or a string.
developer1 = 'Eunice'
developer_tuple = tuple(developer1)
print(developer_tuple) 

#Checking If an Element Is in a Tuple
programming_languages = ('Python', 'Java', 'C++', 'Rust', 'Go', 'Ruby', 'Swift', 'Kotlin', 'PHP', 'TypeScript', 'Scala', 'Perl', 'Haskell', 'Lua', 'Clojure', 'Elixir', 'F#', 'Erlang', 'R')
print('Python' in programming_languages) 
print('JavaScript' in programming_languages)

#unpacking values from a tuple
name, age, profession = developer
print(name)
print(age)
print(profession)

#unpacking values  that are not in order using the * operator to collect the remaining values into a new tuple.
developers_names = ('Eunice', 'John', 'Mary', 'Sarah', 'David')
first_name, *rest = developers_names
print(first_name)
print(rest) # has the rest of the values that were not assigned to the first_name variable in a list.


def item_cost():
    item = 'Laptop'
    cost = 2000
    return item, cost #separating the values with a comma creates a tuple containing the two values.


item_bought = item_cost()
print(item_bought) # returns a tuple containing the item and cost values

x,y = item_cost() #unpacking the tuple returned by the function into two separate variables x and y.
print(x)
print(y)


#slicing tuples
fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')
print(fruits[1:5])





##-------------------------##
#common tuple methods
#count() method returns the number of times a specified value appears in a tuple.
numbers = (1, 2, 3, 4, 5, 1, 2, 1)
count_of_ones = numbers.count(1)
print(count_of_ones) # 3

#index() method returns the index of the first occurrence of a specified value in a tuple.
index_of_three = numbers.index(3)
print(index_of_three) # 2

#finding the index of a value by starting from a specific index when the value appears more than once 
index_of_ones_from_index_3 = numbers.index(1, 3)
print(index_of_ones_from_index_3) # 5

#passing in a start and end index to search for the value within a specific range of the tuple.
index_of_ones_in_range = numbers.index(1, 2, 6)
print(index_of_ones_in_range) # 5

#sorted() function can be used to sort the elements of a tuple and return a new sorted list.
unsorted_tuple = (5, 2, 9, 1, 7)
#the sorted() function can be used without modifying the original tuple 
sorted_list = sorted(unsorted_tuple)
print(sorted_list) 
print(unsorted_tuple) 
# the original tuple remains unchanged


#key = len argument can be used to sort the elements of a tuple based on their length.
words_tuple = ('apple', 'banana', 'kiwi', 'grape', 'orange')
sorted_by_length = sorted(words_tuple, key=len)
print(sorted_by_length) 


#reverse = True argument can be used to sort the elements of a tuple in descending order.

sorted_words = sorted(words_tuple, reverse=True)
print(sorted_words)