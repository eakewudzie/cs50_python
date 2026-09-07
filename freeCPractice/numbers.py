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
