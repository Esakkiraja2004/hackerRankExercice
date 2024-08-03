def swapCase(l):
    a=[]
    for i in range(len(l)): 

        a.append(l[i])
        if a[i].isupper():
            a[i] = a[i].lower()
        else:
            a[i] = a[i].upper()

    l = "".join(a)
    return l

l = "HelloRaja"
print(swapCase(l))