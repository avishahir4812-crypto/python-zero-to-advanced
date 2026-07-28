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

# num1 =(int(input("enter your number1:")))
# num2 =(int(input("enter your number2:")))
# num3 =(int(input("enter your number3:")))

# if(num1>num2 and num1>num3):
#      print(num1,"this number is big")
# elif(num2>num1 and num2>num3):
#     print(num2,"this number is big")
# elif(num3>num2 and num3>num1):
#      print(num3,"this number is big")
# elif(num1 == num2 == num3):
#     print("All numbers are equal")

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))

# if num1 > num2 and num1 > num3:
#     print(num1, "is the biggest number")
# elif num2 > num1 and num2 > num3:
#     print(num2, "is the biggest number")
# elif num3 > num1 and num3 > num2:
#     print(num3, "is the biggest number")
# elif num1 == num2 == num3:
#     print("All numbers are equal")
# else:
#     print("Two numbers are equal and are the largest")

# #voting aligibe

# age =(int(input("enter  your number:")))

# if(age>18):
#     print("aligibke for vote")
# elif(age<18):
#     print("not aligible")
# else:
#     print("not vaild input")

# #number divide with 3 and 5 and both

# num =(int(input("enter your number:")))

# if(num%3==0 and num%5==0):
#     print("number is divisible with both")
# elif(num%3==0):
#     print(num,"number is divisable with 3")
# elif(num%5==0):
#     print(num,"number is divisible with 5")

# else:
#     print("not divisable")

# #grade system

# marks =(int(input("enter your marks:")))

# if(marks>90):
#     print("grade is A")
# elif(marks>70 and marks<90):
#     print("grade is B")
# elif(marks>40 and marks<60):
#     print("garde is C")
# elif(marks>33 and marks<40):
#     print("grade is D")
# else:
#     print("student fail")

#calculator

num1 =(int(input()))
operator =(input("choose your operator;+,-,/,*,% : "))
num2 =(int(input()))

if(operator =="+"):
    print("ans",num1+num2)
elif(operator =="-"):
    print("ans",num1-num2)
elif(operator =="*"):
    print("ans",num1*num2)
elif operator == "/":
    if num2 != 0:
        print("Answer:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
elif(operator =="%"):
    if num2 !=0:
        print("ans:",num1 % num2)
    else:
        print("Error: Modulus by zero is not allowed.")

else:
    print("Invalid operator!")





