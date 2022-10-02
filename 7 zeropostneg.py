print("to check weather given number is Positive Negative ot Zero")
n=int(input("enter the number: "))
match n :
    case n if n>0 :
        print("given number is positive")
    case n if n==0 :
        print("given number is zero")
    case n if n<0 :
        print("given number is negative")