def main():
    y = int(input("Enter a number: "))
    print("the square of " + str(y) + " is: ", square(y))

def square(n):
    #return n * n #return the result of n multiplied by itself   
    return pow(n,2) # an alternative to square
main()