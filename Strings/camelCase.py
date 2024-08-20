def split_by_uppercase(s):
    result = []
    start = 0

    for i in range(1, len(s)):
        if s[i].isupper():
            result.append(s[start:i])
            start = i

    result.append(s[start:])
    return len(result)

print(split_by_uppercase(s))
