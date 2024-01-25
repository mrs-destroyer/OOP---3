# Exception handling in python 
Exception handling in python allows you to separate error-handling code from normal code. An exception is a Python object which represents an error. As with code comments, exceptions help us to remind ourself of what the program expects.  


# User defined Exception
User-defined exceptions are ones that we writes in our code to address particular errors. These exceptions are defined by creating a new class that inherits from the Exception class or one of its subclasses.


# Built-in Exception
Python has a number of built-in exceptions, such as the well-known errors SyntaxError, NameError, and TypeError. These Python Exceptions are thrown by standard library routines or by the interpreter itself. They are built-in, which implies they are present in the source code at all times.

# clean up action
Clean-up actions are the statements that are always executed in a program. Even if the program contains an error, these statements are performed. These statements are also performed if we have implemented exception handling in our program.

# Nzec error
NZEC stands for Non Zero Exit Code. It is a number that is returned by the program to the operating system when it is not able to terminate successfully.

# try and except in Python
The try block lets us test a block of code for errors. The except block lets us handle the error. The else block lets us execute code when there is no error. The finally block lets us execute code, regardless of the result of the try- and except blocks.
