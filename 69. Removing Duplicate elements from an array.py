Link : https://prepinsta.com/python-program/removing-duplicates-elements-from-an-array/


def remove_duplicates(arr):
    new_arr = []
    for element in arr:
        if element not in new_arr:
            new_arr.append(element)
    return new_arr

arr = [10, 20, 40, 30, 50, 20, 10, 20]
print(remove_duplicates(arr))
