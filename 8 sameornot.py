print("enter two string to  check given string are identical or not and print in dictonary order")
n=input("enter first string : ")
m=input("enter second string : ")
match n :
    case n if n==m :
        print("string are identical")
    case n if n>m :
        print(n)
        print(m)
    case n if n<m :
        print(m)
        print(n)