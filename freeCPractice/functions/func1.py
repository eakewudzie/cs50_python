def hello():
    print('hello')




hello()


def calcsum(x,y):
    print(x + y)



calcsum(3, 4)


def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None.      return keyword has to be used here  


#the use of global and local variables in a function

tax_rate = 0.05 #global variable


def cal_tax(price):
    tax = price * tax_rate  #where tax_rate i the local variable here since it is defined outside the function
    return tax


cal_tax(100) 

print(tax_rate) # 0.05
print(cal_tax(100)) # 5.0
