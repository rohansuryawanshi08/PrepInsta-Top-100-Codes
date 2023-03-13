Link : https://prepinsta.com/python-program/remove-all-character-from-string-except-alphabets/

string = "Hello! How are you? 123"
alphabets = ""

for char in string:
    if char.isalpha():
        alphabets += char

print(alphabets)
