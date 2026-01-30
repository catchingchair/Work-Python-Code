

def find_largest(the_strings):
    longest = 0
    for s in the_strings:
        print(len(s))
        if len(s) > longest:
            longest = len(s)
    return longest

test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]
result = find_largest(test_strings)