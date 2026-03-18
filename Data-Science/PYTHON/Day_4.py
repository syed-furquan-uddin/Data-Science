## Write to  a file 
file = open("txt1.txt","w")
file.write("Hello Data science")
file.write("\nPython is a great language")
file.close()

## Read from  a file
file =open("txt1.txt", "r")
content = file.read()
print(content)
file.close()

## Professional Way (Best Practice)
with open("txt1.txt", "r") as file :
    content = file.read()
    print(content)

## Exceptional Handling

"""a = 10
b = 0
print(a/b) # ERROR Division by zero"""

try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid Value")

## Task 1:

file = open("txt2.txt","w")
file.write("Furquan")
file.write("\n I want to become a Data scientist")
file.close()

file = open("txt2.txt", "r")
content = file.read()
print(content)
file.close()

with open("txt2.txt", "r") as file:
    content=file.read()
    print(content)


## Create a Exceptional handling  program 
 
try:
   a = 100
   b = int(input("'Enter the number : "))
   print(a/b)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid Input")