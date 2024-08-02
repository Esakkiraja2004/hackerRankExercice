def pali (n):
    k = True
    for i in range(len(n)):
        string = str(n[i])
        if string == string[::-1] and len(string) > 2:
            k = True
        else:
            k = False
            break
    if k ==  True:
        return True
    else:
        return False
n = [ 7417 ,258952 ,3693 ,1471,58585]
print(pali(n))
