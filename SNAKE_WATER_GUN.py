import random as rand
name=input("Please Enter your name: ")

print(f"Welcome {name} to the Snake, Water, and Gun Game Space !! I hope you will enjoy our Game Space ")

options=["s","w","g"]
comp=options[rand.randint(0,2)]
op='''Please select form the Following options:
        S : Sanke
        w : water
        g : gun '''
print(op)
player=input()

def game(optonX,comp):
    print(f"*****************************computer selected: {comp}**********************************************************")
    optonX=optonX.lower()
    if optonX == comp:
        print("Match Draw")
    elif optonX == "s" and comp=="w":
        print()
    elif optonX == "s" and comp=="g":
        print("Oppss!! You Lost the round ")
    elif optonX == "s" and comp=="w":
        print("Yaay!!! YOu won the round. Lesgoooo")
    elif optonX == "w" and comp=="s":
        print("Oppss!! You Lost the round ")
    elif optonX == "w" and comp=="g":
        print("Yaay!!! YOu won the round. Lesgoooo")
    elif optonX == "g" and comp=="w":
        print("Oppss!! You Lost the round ")
    elif optonX == "g" and comp=="s":
        print("Yaay!!! YOu won the round. Lesgoooo")
    else:
        print("Something went wrong")

game(player,comp)
