print("program which take user's age and display the category of person.")
age=int(input("please enter your age: "))
match age :
    case  age if age <10  :
        print("kid")
    case age if age <20  :
        print("Teen")
    case age if age < 40  :
        print("young")
    case age if age<=60 :
        print("senior citizen")

