#PRIME OR NOT

num=int(input("Enter the no :" ))
flag=False
if num>1:
    for i in range(2,num):#here only num is there becuase of
         #(2,10) means range 2 to 9 only beacuse num it self divisible by it is 10/10 remainder is zero so only(2,num)
        if (num%i)==0:
            flag=True

            break# single number is completly divisible then it is not prime number then break the loop
        

if flag:#it is return as if True means if block is executed
    print(num,"is not prime number")
else:
    print(num,"is prime number")


