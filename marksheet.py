#marksheet

name=str(input("Enter your name :"))
rollno=int(input("Enter the rollno :"))
math=int(input("Enter the marks of math :"))
sci=int(input("Enter the marks of scie :"))
eng=int(input("Enter the marks of eng :"))

total=(math+sci+eng)
per=float(total/3)

print("name is :",name)
print("roll no is :",rollno)
print("math marks is :",math)
print("sci marks is :",sci)
print("eng marks is :",eng)
print("total is :",total)
print("percentage is :",per)