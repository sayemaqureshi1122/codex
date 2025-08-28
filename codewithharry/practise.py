#1]
print("Welcome to the Coding Village! 🥷")

#2]
name = input("What is your name, adventurer?: ")

#3]
print(f"Greetings, {name} Your journey begins now.")

#4] inout and print
print("Welcome, adventurer!")
favcolor = input("what is your fav color adventurer: ")
print(f"Ah, so your favorite color is {favcolor}. Interesting choice!")
age = int(input("what is your age: "))
if age >= 18:
    print("You are an adult adventurer!")
else:
    print("You are still training, young adventurer!")
#5] arthemetic operations
# a, b = map(int, input("enter numbers: ").split())
a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num : "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

#6] loops
n = int(input("enter a num: "))
for i in range(1, n + 1):
    print(i)

#7] Function
def welcome():
    print("Welcome, brave adventurer!")
    print("Your journey continues...")
welcome()

def attack(enemy, weapon):
    if weapon == "sword":
        return(f"You slashed the {enemy}! with a {weapon}")
    elif weapon == "bow":
        return(f"You shot an arrow at the {enemy}")
    elif weapon == "axe":
        return f"You smashed the {enemy} with an {weapon}"
    elif weapon == "magic":
        return f"You cast a powerful spell on the {enemy}!"
    else:
        return(f"You attacked the {enemy} with a {weapon}!")
msg = attack("dragon", 'sword')
print(msg)
msg1 = attack("tree", "axe")
print(msg1)
msg2 =  attack("bird", "bow")
print(msg2)

print("I\nlove\nCodeChef")
print("i", "love", "codechef",sep = "\n")
