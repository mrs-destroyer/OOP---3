# Python Exception Handling
while(True):
    try:
        num = int(input("Enter a Number : "))
        result = 1/num
        print(result)
    except ValueError as e:
        print("Enter a valid value. ")
        print("Try again")
        print(e)
    except ZeroDivisionError as e:
        print("This value is not divided by Zero.")
        print("Try again")
    else:
        break
print("Finished")    


# User defined Exception
age = int(input("Enter Your age : "))
if age < 0:
    print("Invalid Age")
elif age <= 40:
    print("Eligible for riding.")
else:    
    print("Not Eligible.")


# Built-in Exception
'''
There are two types of error:
syntaxerror that we can't handle.
logicalerror that we can handle(exception)
'''

# Nzec error
n = int(input("Enter a number: "))
k = int(input("Enter a number : "))
print(n," ",k)


# try and except in Python
num1 = int(input("Enter First number : "))
num2 = int(input("Enter a Second number : "))
try:
    a = num1/num2
    print("The result is : " , a)
except:
    print("This value can't be divided by zero. ") 

print("Finished")    


# clean up action in python 
try:
    myFile = open("myfile.txt" , "r")
    a= myFile.read()
    print(a)
    myFile.close()
except FileNotFoundError:
    print("The file is not found") 
finally:
    myFile.close()
print("Finished") 

