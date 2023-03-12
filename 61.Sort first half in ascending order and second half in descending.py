Link : https://prepinsta.com/python-program/program-to-sort-first-half-in-ascending-order-and-second-half-in-descending-order-in-an-array/

Def sort_first_half_ascending_second_half_descending(arr):
    # Find the midpoint of the list
    midpoint = len(arr) // 2
    
    # Sort the first half of the list in ascending order
    first_half = sorted(arr[:midpoint])
    
    # Sort the second half of the list in descending order
    second_half = sorted(arr[midpoint:], reverse=True)
    
    # Concatenate the sorted halves and return the result
    return first_half + second_half


print(sort_first_half_ascending_second_half_descending([1,2,3,4,5,6]))
