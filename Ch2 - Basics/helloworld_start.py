#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#

def main():
    print("Hello World!")
    name = input("What is your name? ")
    print("Nice to meet you", name)

# checking to see that the program has been executed, prevents the file from being run on import
if __name__ == "__main__":
    main()