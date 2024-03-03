#series 1
#1*1,2*2-------

n=int(input("Enter the No :"))
for i in range(1,n+1):
    print(i*i,end=" ")

#
n=int(input("\nEnter the No :"))
for i in range(1,n+1):
    print(i,"*",i,"=",i*i)

#1,-4 ,9,-16 -----
n=int(input("Enter the No :"))
for i in range(1,n+1):
    if(i%2==0):#even no logic
        print((-i)*i,end=" ")
    else:
        print((i)*i,end=" ")
           

