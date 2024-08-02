n = [1,2,3,4]
s = 4

first = 0
last = len(n) - 1

while(first <= last):

    mid = (first + last)//2

    if (s == n[mid]):

        print(mid)
        break
    
    elif (s > n[mid]):

        first = mid + 1    

    else:

        last = mid -1
    

else:

        print(False)