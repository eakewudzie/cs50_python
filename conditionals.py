x = int(input("Enter a number ,let us call it x: "))
y = int(input("Enter another number: let us call it y:"))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")




#scores checker
score = int(input("Enter your score: "))
if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else:    
    print("You got an F try harder next time")  