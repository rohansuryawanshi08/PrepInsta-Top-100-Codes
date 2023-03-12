Link : https://prepinsta.com/python-program/finding-repeating-elements-in-an-array/

arr = [10, 20, 40, 30, 50, 20, 10, 20]

for i in range(0,len(arr)):
    for j in range (i+1,len(arr)):
        if (arr[i]==arr[j]):
            print(arr[j])
