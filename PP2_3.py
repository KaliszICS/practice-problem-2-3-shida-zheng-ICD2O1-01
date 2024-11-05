def q1(): 
    # Assignment code for q1
    word = input("In: ")
    if word.endswith("ife"):
        print("-ives")
    elif word.endswith("ey"):
        print("-eys")
    elif word.endswith("y"):
        print("-ies")
    else:
        print("-s")

def q2(): 
    # Assignment code for q2
    num = int(input("In: "))
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")

def q3():
    # Assignment code for q3
    try:
        a = float(input("Input a number: "))
        b = float(input("Input a number: "))
        c = float(input("Input a number: "))
        
        if a + b <= c or a + c <= b or b + c <= a:
            print("No Triangle")
        elif a == b == c:
            print("Equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        else:
            print("Scalene")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Uncomment the following code when running tests
# q1()
# q2()
# q3()
