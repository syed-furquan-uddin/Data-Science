## ATM Machine Simulation Program using conditional statements

balance = 1000
print("Welcome to the ATM Machine")
print("1. Check Balance")
print("2. Deposite")
print("3. Withdraw")

choice=int(input("Enter your choice(1-3) : "  ))
if choice == 1:
    print("your balance is : ", balance)
elif choice == 2:
    amount=int(input("Enter the amount to deposite : "))
    balance += amount
    print("Deposite sucessfully")
    print("your balance is : ", balance)
elif choice  == 3:
    amount=int(input("Enter the amount to withdraw : "))
    if amount <= balance:
        balance -=amount
        print("Withdraw sucessfully")
        print("your balance is : ", balance )
    else :
        print("Insufficient balance")
else :
    print("Invalid Choice")