Link : https://prepinsta.com/python-program/find-a-number-is-palindrome-or-not/
    
def is_palindrom(word):
    reverse_word=word[::-1]
    if reverse_word==word:
        return f"{word} is Palindrom "
    else :
        return f"{word} is not Palindrom"
    
word=input("Enter a Value : ")
print(is_palindrom(word))
