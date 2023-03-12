Link : https://prepinsta.com/python-program/find-non-repeating-elements-in-an-array/

def find_non_repeating_elements(arr):
    non_repeating_elements = []
    for i in range(len(arr)):
        if arr[i] not in arr[i+1:] and arr[i] not in non_repeating_elements:
            non_repeating_elements.append(arr[i])
    return non_repeating_elements

arr = [10, 20, 40, 30, 50, 20, 10, 20]
print(find_non_repeating_elements(arr))
