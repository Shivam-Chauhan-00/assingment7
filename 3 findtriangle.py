print("press 1 to check given sides are right angled triangle or not ")
print("press 2 to check given sides are isosceles triangle or not ")
print("press 1 to check given sides are equilateral triangle or not ")
print("exit")
n=int(input("select the opertion: "))
match n :
    case 1 :
        x=int(input("enter the base :"))
        z=int(input("enter the perpendicular: "))
        y=int(input("enter the hyotenuse: "))
        if y*y == x*x+z*z :
            print("the traingle is right angled trianlge")
        else :
            print("not ringht angle triangle")
    case 3 :
        x=int(input("enter the base :"))
        z=int(input("enter the perpendicular: "))
        y=int(input("enter the hyotenuse: "))
        if x==y==z :
            print("this is an equilateral triangle")
        else :
            print("this is not equilateral triangle")