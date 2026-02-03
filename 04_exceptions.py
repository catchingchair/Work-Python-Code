# Errors can heppen in porgrams, and we need a clean way we can handle them
# This code will cause an error because you can't divide by zero:
# x = 10 / 0

# two parts of exception handeling. 
# 1. The code we want to run
# 2. the code that handles any problems that may occur

# try:
#     x = 10 / 0
# except:
#     print("that did not work.")


try:
    answer = input("What should I divide 10 by? ")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You cannot divide by zero")
except ValueError as e:
    print("You didn't give me a valid number")
    print(e)
finally:
    print("Finally always runs")
