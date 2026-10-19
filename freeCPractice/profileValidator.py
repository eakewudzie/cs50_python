
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