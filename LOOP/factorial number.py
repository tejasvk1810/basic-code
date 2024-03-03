#factorial 
num=int(input("Enter the No :"))
factorial=1
if num<0:
    print("sorry,factorial does not exist for negative number")
elif num==0:
    print("The factorial of zero is 1")
else:
 
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)




