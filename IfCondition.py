a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))


if a>b:
    if a>c:
        print("A Is Max Number")
    else:
        print("C Is Max Number")
elif b>c:
    print("B Is Max Number")
else:
    print("C Is Max Number")
