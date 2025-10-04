scr_Gryffindor = 0
scr_Ravenclaw = 0
scr_Hufflepuff = 0
scr_slythrein = 0
question1 = "Q1) Do you like Dawn or Dusk? \n1) Dawn\n2) Dusk \n"
print(question1)
ans1 = int(input("enter your ans: "))
if ans1 == 1:
    scr_Gryffindor += 1
    scr_Ravenclaw += 1
elif ans1 == 2:
    scr_Hufflepuff += 1
    scr_slythrein += 1
else:
    print("Wrong input")

question2 = "Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) THe Bold\n"
print(question2)
ans2 = int(input("enter your ans: "))
if  ans2 == 1:
    scr_Hufflepuff += 2
elif ans2 == 2:
    scr_slythrein += 2
elif ans2 == 3:
    scr_Ravenclaw += 2
elif ans2 == 4:
    scr_Gryffindor += 2
else:
    print("Wrong input")
    
question3 = "Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"
print(question3)
ans3 = int(input("enter your ans: \n"))
if ans3 == 1:
    scr_slythrein += 4
elif ans3 == 2:
    scr_Hufflepuff += 4
elif ans3 == 3:
    scr_Ravenclaw += 4
elif ans3 == 4:
    scr_Gryffindor += 4
else:
    print("Wrong input")
print("Total scores of all houses:\n")
print(scr_Gryffindor)
print(scr_Hufflepuff)
print(scr_slythrein)
print(scr_Ravenclaw)

