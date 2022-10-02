print("enter two values to perform operation \n 1 addition \n 2 subraction \n 3 divison \n 4 multiplicaton")
n=int(input("enter first no.: "))
m=int(input("enter second no.: "))
x=int(input("enter the operaton no.:"))
match x :
    case 1 :
        print(n+m)
    case 2 :
        print(n-m)
    case 3 :
        print(n/m)
    case 4 :
        print(n*m)
    case _ :
        print("enter a valid operation no.")