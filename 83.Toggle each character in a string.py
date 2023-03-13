Link : https://prepinsta.com/python-program/toggle-each-character-in-a-string/

def toggled_string(n):
    toggled=""
    for i in n:
        if i.islower():
            toggled==toggled+i.upper()
        else:
            toggled=toggled+i.lower()

    return toggled
