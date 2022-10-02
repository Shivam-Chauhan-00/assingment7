print("enter any number like positive negative even odd ")
n=int(input("enter the number: "))
match n :
    case n if n>0 and n%2==0 :
        print("Saurabh Shukla")
    case n if n<0 and n%2 :
        print("Prateek Jain")
    case n if n>0 and n%2 :
        print("Aditya Choudhary")
    case _:
        print("try again")