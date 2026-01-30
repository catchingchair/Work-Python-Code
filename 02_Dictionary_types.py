# Dictionary: a key-value data structure
mydict = {
    "one": 1,
    "two": 2,
    3: "three",
    4.5 : ["four","point","five"]
}

print(mydict)

# dictionaries are accessed via keys
# print(mydict["three"]) # this will not work. ERROR: KeyError: 'three'. looks like you can use the keys in the brackets. 
print(mydict[3])

# you can also set dictionary data by creating a new key
mydict["seven"] = 7
print(mydict)

# Trying to access a nonexistant key WILL produce an error
# print(mydict["foo"]) # KeyError: 'foo'

# To avoid this, you can use the "in" operator to see if a key exists
if ("foo" in mydict):
    print("KEY FOUND!")
else:
    print("KEY NOT FOUND!")
# You can retrieve all of the keys and values from a dictionary
print(mydict.keys())
print(mydict.values())

print("\n=============\n") # for spacing

for key, val in mydict.items(): # another way to print out the items of a list.
    print(val, key)