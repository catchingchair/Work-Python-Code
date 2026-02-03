# Palindromes

def is_palindrome(teststr):
    newstr = ""
    # first strip off any punctuation and convert to lowercase for later comparison
    for l in teststr: 
        if (l != '!' and l != '\'' and l != ',' and l != '.' and l != '?' and l != ' '): # a cleaner way would be to use the isalnum() function. 
            newstr += l.lower()
    # compare to the reversed to catch if its not a palindrome
    for i,l in enumerate(reversed(newstr)):
        if(l != newstr[i]):
            print(f"{l} and {newstr[i]} are not the same! cant be a palindrome!")    
            return False
    return True

check_this = input("Enter a word/phrase: ")
print(is_palindrome(check_this))