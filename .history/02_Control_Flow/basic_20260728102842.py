# #odd even

# num =(int(input("enter your number:")))

# if(num%2==0):
#     print(num,"is even number")
# else:
#     print(num,"is odd nuber")

#positiv,negative and zero

# num =(int(input("enter your number:")))

# if(num>0):
#     print(num,"this is positive number")
# elif(num<0):
#     print(num,"this is nagetive number")
# else:
#     print(num,"this is 0")

#big number of them

num1 =(int(input("enter your number1:")))
num2 =(int(input("enter your number2:")))
num3 =(int(input("enter your number3:")))

if(num1>num2 and num1>num3):
     print(num1,"this number is big")
elif(num2>num1 and num2>num3):
    print(num2,"this number is big")
elif(num3>num2 and num3>num1):
     print(num3,"this number is big")
elif(num1 == num2 == num3):
    print("All numbers are equal")