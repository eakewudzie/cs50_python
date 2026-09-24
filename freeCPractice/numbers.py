#integers and floats
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

#floor division is a mathematical operation that divides one number by another and rounds down the result to the nearest whole number. It is denoted by the double forward slash (//) operator in Python.   
#returns the largest integer less than or equal to the result of the division.
floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

#exponentiation, raising the number to the power of another number
exp_int = my_int_1 ** my_int_2
exp_float = my_float_1 ** my_float_2

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0‚

#there is a way to convert a float to an int and vise versa. This is called type casting. int() and float() funcs

int_m = 2.3222

rounded_int_m = round(int_m)

print(rounded_int_m)

#exponentiation using the pow() function, which takes two arguments: the base and the exponent. It returns the result of raising the base to the power of the exponent.                      
num1 = 5.6
num2 = 2

num1_exp = pow(num1, num2) # 5.6 raised to the power of 2
print('Exponentiation:', num1_exp)



#rounding numbers
numx = 3.14159
numw = 2.71828

rounded_numx = round(numx, 2) #rounds to 2 decimal places
rounded_numw = round(numw) #rounds to 3 decimal places
print('Rounded numx:', rounded_numx) # Rounded numx: 3.14
print('Rounded numw:', rounded_numw) # Rounded numw: 3




#augmented assignment : a shorter way to update a variable using its current value

x = 10
x += 56
print('x value:', x)


# augmented: multiplication
productX = 5
productX *= 3
print('ProductX value:', productX) # ProductX value: 15