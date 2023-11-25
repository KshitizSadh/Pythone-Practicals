#  we will find the value of d in using quadratic formula
a = int(input("Enter the co-efficient of x**2 : "))
b = int(input("Enter the co-efficient of x: "))
c = int(input("Enter the constant term: "))
d = b**2 - 4*a*c
if d == 0 or d > 0 :
    x1 = float((-b + (d)**0.5/2*a))
    x2 = float((-b - (d)**0.5/2*a))
    print(x1,x2)
elif d < 0 :
    print("the eqn has no solution")

