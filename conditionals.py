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
    print("You got an F try harder next time. You can do it. More practice and you will get better.")  






#program that checks for whether or not a number is even or odd.... using two functions.
#one checking if number is even or odd and the other function to call the first function and print the result.

def main():
    num1= int(input("Enter a number:"))
    if is_even(num1):
        print("The number is even")
    else:
        print("The number is odd")

  



def is_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
    #return True if num % 2 == 0 else False

    return num % 2 == 0.  # this is another way of writing the same thing as the above code. It is a more concise way of writing it. 

    

main()