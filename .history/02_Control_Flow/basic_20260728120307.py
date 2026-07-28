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

# num1 =(float(input("enter num1")))
# operator =(input("choose your operator;+,-,/,*,% : "))
# num2 =(float(input("enter your num2")))

# if(operator =="+"):
#     print("ans",num1+num2)
# elif(operator =="-"):
#     print("ans",num1-num2)
# elif(operator =="*"):
#     print("ans",num1*num2)
# elif operator == "/":
#     if num2 != 0:
#         print("Answer:", num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")
# elif(operator =="%"):
#     if num2 !=0:
#         print("ans:",num1 % num2)
#     else:
#         print("Error: Modulus by zero is not allowed.")

# else:
#     print("Invalid operator!")

#leap year

# year =int(input("enter your year:"))

# if(year%4== 0):
#     print(year,"leap year")
# else:
#     print(year,"not leap year")


#largest number of in 3 number

# num1 =(int(input("enetr your number:")))
# num2 =(int(input("enter your number2:")))
# num3 =(int(input("enter your number3:")))

# if(num1>num2 and num1>num3):
#     print(num1,"is big")
# elif(num2>num1 and num1>num3):
#     print(num2,"is bih")
# elif(num3>num1 and num3>2):
#     print(num3,"is big")

#login

# username =(str(input("enter your username;")))
# password =(int(input("enter your pasword:")))

# if(username =="admin"):
#     if(password !="123"):
#         print("password inccrect")
# else:
#     print("login sucessfully")

#incometex calculator

# income =(int(input("enter year anual income:")))

# phase1 = income * 0.05   # 5%
# phase2 = income * 0.10   # 10%
# phase3 = income * 0.20   # 20%

# if(income>50000 and income<75000):
#     print(phase1,"is your tex")
# elif(income>50000 and income<100000):
#     print(phase2,"is your tex")
# elif(income>100000):
#     print(phase3,"is your tex")
# else:
#     print(income,"is not reqiure amounte to tex")

#elctric bill

unit = (int(input("enter your unit:")))

phase1 = unit*5
phase2 = unit*7
phase3 = unit*10

if(unit<100):
    print(phase1,"your bill amount")
elif(unit>101 and unit<200):
    print(phase2,"your bill amount")
elif(unit>201 and unit<300):
    print(phase3,"your bill amount")