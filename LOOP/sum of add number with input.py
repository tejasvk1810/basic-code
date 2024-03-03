#sum of odd number with input

n=int(input("Enter the No. :"))
s=0
for i in range(1,n+1):
    if(i%2!=0):
        print(i,end=" ")
        s+=i
print("\n Sum of odd no :",s)        

#sum of even number with input

n=int(input("Enter the no:"))
s=0
for i in range(1,n+1):
    if(i%2==0):
        print(i,end=" ")
        s+=i#s=s+i
print("\n Sum of even no :",s)           




