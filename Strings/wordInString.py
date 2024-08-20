q = int(input())
for i in range(q):
    s = input()
    l = list("hackerrank")
    for char in s:
        if l and char == l[0]:
            l.pop(0)
    if not l:
        print("YES")
    else:
        print("NO")
