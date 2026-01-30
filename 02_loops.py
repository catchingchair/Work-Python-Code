# Loops

x = 0

# 1. while loop
# while x < 5:
#     print(x)
#     x+=1

# answer = input("Should I stop? ")
# while answer != "yes":
#     print(answer)
#     answer = input("Should I stop? ")

# 2. for loop

# days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# for d in days:
#     print(d)

# 3. use the break and continue statements

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# for d in days:
#     if (d == "Tue"):
#         continue
#     print(d)

# 4. using the enumerate() function to get an index and an item
#       - built in python function. enumerate returns the index value.
for i,d in enumerate(days):
    print(i,d)
