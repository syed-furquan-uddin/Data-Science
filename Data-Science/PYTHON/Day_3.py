## Simple function
 
def greet():
    print("Hello Furquan ")
greet()

## Function with parameter

def add(a,b):
 return a+b
result = add(5,10)
print(result)

## List 

numbers=[10,20,30,40,50]
print(numbers)
## Accessing Elements
print(numbers[0])
print(numbers[1])

## Looping through List
for num in numbers:
   print(num)

## Real Data Science Example 

marks = [75,80,60, 90]
print(sum(marks))

## Dictionaries

student= {
   "name":"Furquan","age":23, "course":"MCA"
   }
print(student["name"])
print(student["age"])

## Real Life Exapmle 


students = [
    {"name": "Furquan", "marks": 75},
    {"name": "Ali", "marks": 60},
    {"name": "Ahmed", "marks": 76}
]

for student in students:
    print(student["name"],student["marks"])

## Task 1:
## Create a function take a list of numbers and return the average 

def avg(numbers):
   return sum(numbers)/len(numbers)
numbers = [10,20,30,40,50]
print(avg(numbers))

## Task 2:
## Create a Dictionary program 

student ={
   "name ":"furquan ",
   "age ": 23,
   "skills":"python,machine learning , data science",
   "Dream Company ": "Google "
}
print(student)

## task 3 (Mini Project):
## Create a program store 5 students marks in list and print highest marks , Lowest marks and Average marks .

marks = [75,80,60,90,85]
print("Highest marks :", max(marks))
print("Lowest marks :" ,min(marks ))
print("Average marks: ", sum(marks)/len(marks))
