# Built-in Functions

mystring = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,2,5,6,9,12,14,17,20,30]

# len() is a function that will return the length (as an integer) of an object
print(len(mystring))

# max() is a function that will return the max value of an object
print(max(mystring))

# min() is a function that will return the min value of an object
print(min(mynumbers))

# str() is a function that will return a string version of an object
prefix = "result: "
result = 5
print(prefix + str(3.1415))

# range(start,stop,step) will create a range of numbers (ending value not included)
# you can use ranges along with loops
for i in range(5,15):
    print(i)

print("\n============\n")

for i in range(5, len(mystring),2):
    print(mystring[i])




