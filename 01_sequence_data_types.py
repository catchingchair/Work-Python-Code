# Sequence Data Types

# Sequences: List and Tuples

mylist = [0, 1, "two", 3.2, False]
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[2])
print(mylist[-1]) # this will print from the end of the list. in this case it would print "False"
mylist[0] = 10
print(mylist)

# the first number is the starting index
# the second number is the ending index (non-inclusive)
# the third number is the step

# syntax [start:stop:step]

print(mylist[1:4])

# Sets - they can only contain unique values. they will force uniqueness.
# Set objects are not subscriptable! they do not support indexing. 
myset = {1, 4, 0, 5, 4, 4, 2, 3}
print(myset)

# tuples - they are like lists but they are immutable (an object with a fixed value, cannot be altered. numbers and strings are also immutable.)
mytuple = (0,1,2,"three")
print(mytuple[1])

x = 5639021
# print(x[1]) # this will cause an error. integers are not subscriptable. 

	

