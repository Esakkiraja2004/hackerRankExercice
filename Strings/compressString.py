s = '112223444'
arr = []
i = 0
n = len(s)
while i < n:
    count =1
    for j in range(i+1,n):
        if s[i] == s[j]:
            count+=1
        else:
            break
    arr.append((count,int(s[i])))
    i+=count
for i in arr:
    print(f"({i[0]},{i[1]})")
