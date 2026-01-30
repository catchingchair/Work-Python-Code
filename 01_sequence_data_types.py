# Sequence Data Types

# Sequences: List and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[2])
print(mylist[-1]) # this will print from the end of the list. in this case it would print "False"
mylist[0] = 10
print(mylist)

#accessing a member of a sequence is the same for strings. cannot change the individual values though
