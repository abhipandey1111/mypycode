import random
a = 0
humanscore = list()
times = print(int(input("how many times you want to play")))
elements = ["r", "p", "s"]
while a <= 10:
    y = ("you won")
    l = ("you lose")
    t = ("tie")
    print("-------------------------")
    print("chosse one among r,p,s")
    print("-------------------------")
    user = input()
    computer = random.choice(elements)
    print("-------------------------")
    print("you took", user)
    print("computer took", computer)
    print("-------------------------")
    if computer == user:
        print("the match tie")
        a = a+1
        
    if computer == "r" and user == "s":
        print("you lose")
        a = a+1
        humanscore.append(l)

    if computer == "r" and user == "p":
        print("you win")
        a = a+1
        humanscore.append(y)
    if computer == "s" and user == "p":
        print("you lose")
        a = a+1
        humanscore.append(l)
    if computer == "s" and user == "r":
        print("you win")
        a = a+1
        humanscore.append(y)
    if computer == "p" and user == "r":
        print("you lose")
        a = a+1

        humanscore.append(l)
    if computer == "p" and user == "s":
        print("you win")
        humanscore.append(y)

    if a >= 10:
        break

u= humanscore.count(y)
v=humanscore.count(l)
print("\n\n\n over all score ")
print("-----------------------")
print("your total score:",u)
print("computer total score:",v)
print("------------------------")
if u>v:
    print("you won this tournament")
    print("--------------------------")
else: print("you lose the tournament") 
print("-------------------------")   