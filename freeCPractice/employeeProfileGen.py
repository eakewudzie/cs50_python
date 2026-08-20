first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) +' years old'
print(employee_info)

experience_years = 5


experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

employee_card = f'Employee: {full_name}'
# print(employee_info + str(employee_age) + ' years old and lives at ' + address)

position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card) # Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000.   ... could be updated to include address and experience years if needed.



employee_code = 'DEV-2026-JD-001'
#slicing
#start is the index where the slice begins (inclusive).
#stop is the index where the slice ends (exclusive).
department = employee_code[0:3]
print(department)

#the use of slice 
year_code = employee_code[4:8]
initials = employee_code[9:11]

print(year_code)
print(initials)


#negative index slicing...printing last number or character .....
last_three = employee_code[-3:]
print(last_three)