Link : https://prepinsta.com/python-program/to-sort-array-according-to-the-order-defined-by-another-array/


from collections import Counter

def solve(arr1, arr2):
    res = []
    
    f = Counter(arr1)
     
    for i in arr2:
       
        res.extend([i]*f[i])
         
        f[i] = 0
         
    rem = list(sorted(filter(lambda x: f[x] != 0, f.keys())))
     
    for i in rem:
        res.extend([i]*f[i])
         
    return res
 
 
arr1 = [ 20, 1, 20, 5, 7, 1, 9, 39, 6, 18, 18 ];
arr2 = [ 20, 1, 18, 39 ];
print(*solve(arr1, arr2))
