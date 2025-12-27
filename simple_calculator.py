def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print("Select Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Select 1/2/3/4: ")
    # print(choice)

    if choice in ("1","2","3","4"):
        try: 
            num1 = float(input("Enter a first number: "))
            num2 = float(input("Enter the second number: "))
        except:
            print("Enter the correct value")
            # continue
            
        if choice=="1":
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=="2":
            print(num1,"-",num2,"=", sub(num1,num2))
        elif choice=="3":
            print(num1,"*",num2,"=", mul(num1,num2))
        elif choice=="4":
            print(num1,"/",num2,"=", div(num1,num2))

        next_cal = input("Let's do next calculation? (Yes/No): ").lower()
        if next_cal == 'no':
            break
    
    else:
        print("Invalid Input")
