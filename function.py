#function for hello
def hello(to="world"): #giving it a default value of world just incase user forgets to input
    print("hello" , to)

hello()
name = input("What is your name? ")
hello(name)