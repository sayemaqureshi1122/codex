# first_name = "tony"
# last_name = "stark"
# age = 51
# is_genius = True
# print(first_name, last_name, is_genius)

# super_hero = input("what is your superhero name? ")
# print("Hello " + super_hero)

# first = int(input("enter a num: "))
# second = int(input("enter a num: "))
# print("result is : " + str(first + second))
# print(super_hero.find('T'))

#building a calculator
num1 = int(input())
num2 = int(input())
operation = input("enter operation u want to perform: (ie. sum, subtract, multiplication, division, power, mod): ")
def cal(num1, num2, operation):
    if operation == "sum":
        print(num1 + num2)
    elif operation == "subtract":
        print(num1 -  num2)
    elif operation == "division":
        if num2 > 0:
            print(num1 / num2)
        else:
            print("division with 0 is invalid")
    elif operation == "multiplication":
        print(num1 * num2)
    elif operation == "mod":
        if num2 > 0:
            print(num1 // num2)
        else:
            print("division with zero is invalid")
    elif operation == "power":
        print(num1 ** num2)
    else:
        print("invalid operation")
cal(num1, num2, operation)
