import UDF


while True:
    print("*"*40)
    print("1. OddEven")
    print("2. Max Of 2")
    print("3. Max Of 3")
    print("4. Exit")
    print("*"*40)
    choice=int(input("Enter Your Choice : "))
    print("*"*40)
    if choice==1:
        n1=int(input("Enter Value : "))
        UDF.oddeven(n1)
        print("*"*40)
    elif choice==2:
        n1=int(input("Enter Value : "))
        n2=int(input("Enter Value : "))
        UDF.maxof2(n1,n2)
        print("*"*40)
    elif choice==3:
        n1=int(input("Enter Value : "))
        n2=int(input("Enter Value : "))
        n3=int(input("Enter Value : "))
        UDF.maxof3(n1,n2,n3)
        print("*"*40)
    elif choice==4:
        print("Thank You For Using Our Services.")
        break
    else:
        print("Invalid Choice. Please Try Again.")
