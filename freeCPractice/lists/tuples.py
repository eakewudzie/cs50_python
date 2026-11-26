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


