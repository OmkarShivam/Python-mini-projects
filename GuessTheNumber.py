import random
num = random.randint(1,11)

game=1
chance=1
while game == 1:
    opt=int(input("Guess the Number if you can "))
    if opt == num:
        print(f"wwowww!!! you got the number!. You took {chance} Chances")
        game=0
    elif opt > num:
        print("No no no!! Your number is graeter than the correct number. Kinndly try again ")
        chance +=1
    else:
        print("No no no!! Your number is smaller than the correct number. Kinndly try again ")
        chance +=1    
