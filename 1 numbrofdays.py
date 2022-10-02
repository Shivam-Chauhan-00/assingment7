print("enter the months no. to check the days")
n=int(input("enter the value: "))
match n :
    case 1 :
        print("this months 31 days")
    case 2 :
        print("this months 28 days")
    case 3 :
        print("this months 31 days")
    case 4 :
        print("this months 30 days")
    case 5 :
        print("this months 31 days")
    case 6 :
        print("this months 30 days")
    case 7 :
        print("this months 31 days")
    case 8 :
        print("this months 31 days")
    case 9 :
        print("this months 30 days")
    case 10 :
        print("this months 31 days")
    case 11 :
        print("this months 30 days")
    case 12 :
        print("this months 31 days")
    case _ :
        print("you didn't entered a valid months number.")