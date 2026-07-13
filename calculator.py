x = 3
u = 2

print(x + u)


w = input("Enter a number: ")
y = input("Enter another number: ")
#convert user input to integer and add them together 
z = int(w) + int(y)

print(z)

print("let us try another calculation now ...")

#making it simpler 
#another alternative to convert user input to integer and add them together
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(a + b)


j = float(input("Enter a number: "))
k = float(input("Enter another number: "))
# w = round(j + k, 1)
# print(f"{w:,.1f}".replace(".", " ,")) 

w = round(j + k, 1)
#applying german formatting of figures to the result of the addition of j and k which are decimals 
# First .replace(",", "X") turns all commas into X
# Then .replace(".", ",") turns all dots into commas
# Finally .replace("X", ".") turns the temporary X values into dots

print(f"{w:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))





