
#update the code, split....etc

email = 'alice.johnson@company.com'
print(f'Email: {email}')

at_position = email.find('@')
print(f'Position of @: {at_position}')

username = email[:at_position]
print(f'Username: {username}')

has_at = '@' in email
print(f'Has @ symbol: {has_at}')


has_com = '.com' in email

print(f'Has .com: {has_com}')

messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

clean_name = messy_name.title()


clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")



messy_email = '  SARAH.DAVIS@COMPANY.COM  '
clean_email= messy_email.strip().lower()

print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'" )


name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')

at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]

print(f'Email: {clean_email}')
print(f'Username: {email_user}')

display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')

phone = '123-456-7890'
phone_clean = phone.replace('-', '')
print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')


full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')

rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

employee_code = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')
ends_with_com = clean_email.endswith('.com')

print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')#starts_with_emp is a boolean variable that checks if the employee_code starts with 'EMP' and returns True or False.
print(f'Clean email: {clean_email}') #clean_email is a string variable that contains the cleaned email address.
print(f'Ends with .com: {ends_with_com}')#ends_with_com is a boolean variable that checks if the clean_email ends with '.com' and returns True or False.

dot_count = clean_email.count('.')
dash_count = employee_code.count('-')#counts the number of dashes in the employee_code and returns an integer value.

print(f'Dots in email: {dot_count}')
print(f'Dashes in code: {dash_count}')