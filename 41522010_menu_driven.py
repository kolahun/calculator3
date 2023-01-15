import math
print("Program by:-ALOK YADAV\nemail=btech41522010@dseu.ac.in")

l=[]
def addition(x,y):
    sum=0
    sum=x+y 
    print(f"THE SUM of {x} + {y} = ",sum)
    l.append(sum)
    
def subtraction(sub1,sub2):
    sub=sub1-sub2
    print(f"THE SUBTRACTION of {sub1} - {sub2} = ",sub)
    l.append(sub)

def  multiple(a,b):
    multi=a*b
    print(f"THE MULTIPLICATION {a} x {b} = ",multi)
    l.append(multi)

def division(a,b):
    div=a/b
    print(f"HE DIVISION {a} / {b} = ",div)
    l.append(div)

def sqrt(a):
    root=math.sqrt(a)
    print(f"THE SQUARE ROOT of {a} = ",round(root,3))
    l.append(root)

def square(num1):
    sq=num1**2
    print(f"THE SQUARE {num1} = ",sq)
    l.append(sq)

def sub_menu():
    while True:
        print("\t\t\t|     -X-X-X-X--SUB MENU--X-X-X-X-     |")
        print("\t\t\t|Press 1 to perform addition           |")
        print("\t\t\t|Press 2 to perform subtraction        |")
        print("\t\t\t|Press 3 to perform multiplication     |")
        print("\t\t\t|Press 4 to perform division           |")
        print("\t\t\t|Press 5 to perform square root        |")
        print("\t\t\t|Press 6 to perform square             |")
        print("\t\t\t|Press 7 to clear & return to main menu|")

        k=float(input("\t\t\tEnter the number for the sub menu "))
        if k==1:
            numadd=float(input("Enter the number to add "))
            addition(float(l[-1]),numadd)

        elif k==2:
            numsub=float(input("Enter the number to subtract "))
            subtraction(float(l[-1]),numsub)

        elif k==3:
            nummulti=float(input("Enter the number to mutiple  "))
            multiple(float(l[-1]),nummulti)
            numdiv=float(input("Enter the number to divide "))

        elif k==4:
            numdiv=float(input("Enter the number to divide "))
            division(float(l[-1]),numdiv)

        elif k==5:
            sqrt(float(l[-1]))

        elif k==6:
            square(float(l[-1]))

        elif k==7:
            l.clear()
            print("\tReturning to the main menu ")
            break

        else:
            print("\tEnter the valid options ")
        
while True:
    print("-+"*20)
    print("{-----------------MAIN MENU----------------}")
    print("{  Press 1 to perform addition             }")
    print("{  Press 2 to perform subtraction          }")
    print("{  Press 3 to perform multiplication       }")
    print("{  Press 4 to perform division             }")
    print("{  Press 5 to perform square root          }")
    print("{  Press 6 to perform square               }")
    print("{  Press 7 to end the tasks                }")
    print("{------------------------------------------}")

    n=float(input("Select the operation you want to perform-->>  "))
    print("-+"*20)
    if n==1:
        num1=float(input("Enter the first number you want to add-->>  "))
        num2=float(input("Enter the second number you want to add-->>  "))
        addition(num1,num2)
        sub_menu()
    
    elif n==2:
        sub1=float(input("Enter the 1st number you want to subtract-->>  "))
        sub2=float(input("Enter the 2nd number you want to subtract-->>  "))
        subtraction(sub1,sub2)
        sub_menu()

    elif n==3:
        num1=float(input("Enter the 1st number-->>  "))
        num2=float(input("Enter the 2nd number-->>  "))
        multiple(num1,num2)
        sub_menu()

    elif n==4:
        num1=float(input("Enter the divisor-->>  "))
        num2=float(input("Enter the divident-->>  "))
        division(num1,num2)
        sub_menu()

    elif n==5:
        num1=float(input("Enter the number you want the square root of-->>  "))
        sqrt(num1)
        sub_menu()

    elif n==6:
        num1=float(input("Enter the number you want to get square of-->>  "))
        square(num1)   
        sub_menu()

    elif n==7:
        print("------------Thank you------------")
        break

    else:
        print("####---WARNING---###")
        print("Enter the valid option  ")
