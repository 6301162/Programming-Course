# Make sure you are not modifying the method signatures
# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    print ("Hello, World!")
   

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.


def myinput_output():

 # Getting input from the user

 name = input("Enter your name: ")
 
 age = int (input("Enter your age:"))

 height = float(input("Enter your height: "))


 # Outputting the collected data

 print(f"Hello, {name}!")

 print(f"You are {age} years old.")

 print(f"Your height is {height} meters.")

myinput_output()
hello_world()
