# Conditionals

x, y = 10, 100
# a = 12, b = 13, c = 15 # cannot assign variables like this becase it tries to assign to a tuble containing literals.

if x < y:
    print("x is less than y")
elif x == y:
    print("x is the same a s y")
else:
    print("x is greater than y")

# conditional statements let you use "a if C else b"
result = "x is less than y" if (x < y) else "x is greater or equal to y"
print(result)