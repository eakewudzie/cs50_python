name = input("What is your name? ")

match name:
    case "Eunice":
        print("Hello Eunice, you are welcome to the program.")
    case "John":
        print("Hello John, you are welcome to the program.")
    case "Alice":
        print("Hello Alice, you are welcome to the program.")
    case _:     
        print("Sorry, your name cannot be found on the program list.")