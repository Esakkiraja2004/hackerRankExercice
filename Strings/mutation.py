def mutation(string,k,n):
    arr = list(string)
    arr[n] = k
    return "".join(arr)
string = "meowww"
k= '!'
n=5
print(mutation(string,k,n))