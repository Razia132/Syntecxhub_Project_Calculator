def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: Division by zero is not allowed"
    return a/b
def calculator():
    while True:
        print("\n --------- CALCULATOR ---------")
        print("Hey there here are some operations you can use :)")
        print("1.Addition (+)")
        print("2.Subtract (-)")
        print("3.Multiply (*)")
        print("4.Divide (/)")
        print("5.Exit")
        choice=input("Enter your choice (1-5) :")
        if choice=="5":
            print("Thank you for using the calculator !")
            break
        if choice not in ["1","2","3","4"]:
            print("Invalid choice.Please try again .")
            continue
        try:
            num1=int(input("Enter the first number :"))
            num2=int(input("Enter the second number :"))
        except ValueError:
            print("please enter valid numeric values.")
            continue

        if choice=='1':
            result=add(num1,num2)
        elif choice=='2':
            result=subtract(num1,num2)
        elif choice=='3':
            result=multiply(num1,num2)
        elif choice=='4':
            result=divide(num1,num2)
        print("Here's the answer :",result)

calculator()
