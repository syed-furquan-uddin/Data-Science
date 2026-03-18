## arithemetic operator 

a= 10
b= 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)

## comparison operator 

print(10>5)
print(10<5)
print(10==5)
print(10!=5)

## Conditional statements

num = 10
if num > 0:
  print("Positive Number")
else:
  print("Negative Number")

marks = 40

if marks >= 35:
  print("Pass ")
else:
  print("Fail")

## Loop

for i in range(5):
    print(i)

## while loop

count = 0
while count < 5 :
  print(count)
  count+=1

## Task 1:
## check if a number is even or odd

num = 10
if num % 2==0:
  print("Even Number")
else:
  print("Odd number")

## Task 2:
## print number from 1 to 10 using loop.

for i in range(1,11):
    print(i)

## Task 3:
## wrrite  a program a take number and print multiplication table of that number(1-10)

num = 5
for i in range(1,11):
  print(num,"x",i,"=",num*i)

