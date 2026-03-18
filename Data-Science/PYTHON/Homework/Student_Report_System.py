## Student Report System

def student_report():
    name = (input("Enter the name : "))
    marks = [int(input(f"Enter the marks {i+1}: "))for i in range(3)]

    total = sum(marks)
    average =total /len(marks )
    result = "Pass" if average >=33 else "Fail"

    print("\n-------Report-------")
    print("NAme : ", name )
    print("Marks : ", marks )
    print("Toatal : ", total )
    print("Average : ", average )
    print("Result : ",result)

student_report()