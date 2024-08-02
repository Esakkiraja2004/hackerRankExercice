b = [1,2,3,5,6]
left = 0
right = len(b)-1

while left <= right:
    # temp  = b[left]
    # b[left] = b[right]
    # b[right] = temp
    b[left],b[right] = b[right],b[left]
    left += 1
    right -=1
print(b)
