name = "Eunice Ewudzie"
age = 28

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # Eunice Ewudzie28


lWord = "ha"
lWordMul = lWord * 3  # Multiply the string by 3
print(lWordMul)


#sting methods
my_full_name = "Eunice Ewudzie"
new_full_name = my_full_name.replace("Ewudzie", "Smith")  # Replace "Ewudzie" with "Smith"
print(new_full_name)


#split method
my_full_name = "Eunice Ewudzie"
name_parts = my_full_name.split()  # Split the string into a list of words
print(name_parts)  # ['Eunice', 'Ewudzie']


my_list = ["Eunice", "Ewudzie", "Smith"]
new_list = " ".join(my_list)  # Join the list into a single string with spaces
print(new_list)  # Eunice Ewudzie Smith 