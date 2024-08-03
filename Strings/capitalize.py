def capitalize(a):
    arr =a.split(" ")
    for i in range(0,len(arr)):
        arr[i] = arr[i].capitalize()
    return " ".join(arr)

a= "hello raja"
 
print(capitalize(a))