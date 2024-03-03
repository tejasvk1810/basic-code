#swap the number
#using temp variable
a=12
b=34
print("before swaping")
print("value of a is :",a)
print("value of b is :",b)
temp=a
a=b
b=temp
print("after swaping")
print("value of a is :",a)
print("value of b is :",b)

#without using temp varaible swapping

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
print("before swaping")
print("value of a:",a)
print("value of b:",b)

a=a+b
b=a-b
a=a-b
print("after swapping")
print("value of a:",a)
print("value of b:",b)

#convert rupee to paisa
amt=float(input("Enter the amount : "))
rupee=int(amt)#amount converted into interger suppose 12.53 -->12
ps=int((amt-rupee)*100)
print("amount:",amt)
print("rupees:",rupee)
print("paisa:",ps)


