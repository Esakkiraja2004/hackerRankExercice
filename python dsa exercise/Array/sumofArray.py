def sum(arr):
    s= 0
    for i in range(len(arr)):
        s += arr[i]
    return s
n = [1,2,3]
print(sum(n))