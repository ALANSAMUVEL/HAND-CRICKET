import random
print("wanna play hand-cricket ?")
print()
user_opinion=input("enter y to continue or press any key to exit :  ").lower()
print()
if(user_opinion!="y"):
    quit()
while True:
    odd_even=input("enter Odd or Even :  ").lower()
    choice=['odd','even']
    if odd_even in choice:
        if(odd_even=="odd"):
            print("computer is  even and user is odd")
        elif(odd_even=="even"):
            print("computer is odd and user is even")
        break
    else:
        continue
    
numbers=[1,2,3,4,5,6]
while True:
    get_num=int(input("enter a num 1 to 6 :  "))
    if get_num not in numbers:
        continue
    break
        
r=random.randint(0,5)
my_num=numbers[r]
print("computer num is ",my_num)
check=get_num+my_num
if(check%2==0):
    print("it's even")
    if(odd_even=="even"):
        while True:
            user=input("user, choose batting or bowling:  ").lower()
            if(user!="batting" and user!="bowling"):
                continue
            break
        if(user=="batting"):
            comp="bowling"
        else:
            comp="batting"
    else:
        print(" computer will choose batting or bowling")
        print("so...computer is batting")
        print("user will bowl")
        comp="batting"
        user="bowling"
elif(check%2==1):
    print("it's odd")
    if(odd_even=="odd"):
        while True:
            user=input("user, choose batting or bowling:  ").lower()
            if(user!="batting" and user!="bowling"):
                continue
            break
        if(user=="batting"):
            comp="bowling"
        else:
            comp="batting"
    else:
        print("computer will choose batting or bowling")
        print("so...computer is batting")
        print("user is bowling")
        comp="batting"
        user="bowling"

if(comp=="batting"):
    n=0
    i=1
    score1=1
    score2=1
    while (i>n):
        s=random.randint(0,5)
        my_num=numbers[s]
        num=int(input("enter a number  :"))
        if num not in numbers:
            print("enter number 1 to 6  :")
            continue
        print("computer number is :",my_num)
        if(my_num!=num):
            score1=score1+my_num
            print("COMPUTER SCORE IS ",score1)
            print()
            i=i+1
        else:
            print("\t\t\t\t  COMPUTER IS OUT  \t\t\t\t")
            break
    print("COMPUTER TOTAL SCORE IS ",score1)
    print("\t\t\t\t NOW USER  IS BATTING \t\t\t\t")
    print()
    while (i>n):
        s=random.randint(0,5)
        my_num=numbers[s]
        ur_num=int(input("enter a number  :"))
        if ur_num not in numbers:
            print("enter a number 1 to 6  :")
            continue
        print("computer num is :",my_num)
        print()
        if(my_num==ur_num):
            print("\t\t\t\t USER IS OUT \t\t\t\t")
            break
        else:
            score2+=ur_num
            continue
    print(" USER TOTAL SCORE IS",score2)
    if(score1>score2):
        print("\t\t\t\t COMPUTER WINS \t\t\t\t")
    elif(score1==score2):
        print("\t\t\t\t DRAW\t\t\t\t")
    else:
        print("\t\t\t\t USER WINS \t\t\t\t")

elif(comp=="bowling"):
    n=0
    i=1
    score1=1
    score2=1
    while (i>n):
        s=random.randint(0,5)
        my_num=numbers[s]
        ur_num=int(input("enter a number  : "))
        if ur_num not in numbers:
            print("enter a number 1 to 6  : ")
            continue
        print("computer num is : ",my_num)
        print()
        if(my_num==ur_num):
            print("\t\t\t\t USER  IS OUT \t\t\t\t")
            print()
            break
        else:
            score1+=ur_num
            print("USER SCORE IS",score1)
            continue
    print("USER TOTAL SCORE IS  :  ",score1)
    print("NOW  USER  WILL BOWL")
    while (i>n):
        s=random.randint(0,5)
        my_num=numbers[s]
        num=int(input("enter a number : "))
        if num not in numbers:
            print("enter a number 1 to 6  : ")
            continue
        print("computer number is : ",my_num)
        if(my_num!=num):
            score2=score2+my_num
            print("COMPUTER SCORE IS",score2)
            i=i+1
        else:
            print("\t\t\t\t COMPUTER IS OUT \t\t\t\t")
            break
    print("COMPUTER TOTAL SCORE IS ",score2)
    if(score1>score2):
        print("\t\t\t\t USER WINS \t\t\t\t")
    elif(score1==score2):
        print("\t\t\t\t DRAW\t\t\t\t")
    else:
        print("\t\t\t\t COMPUTER WINS \t\t\t\t")

    




        
