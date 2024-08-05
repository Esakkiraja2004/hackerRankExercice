def merge(a):
    # Length of each substring
    k = 3
    
    # List to store the substrings with unique characters
    result = []

    # Loop to separate the string into substrings of length k
    for i in range(0, len(a), k):
        substring = a[i:i+k]
        seen = set()
        unique_substring = ''
        for char in substring:
            if char not in seen:
                seen.add(char)
                unique_substring += char
        result.append(unique_substring)
    
    # Print each unique substring
    for r in result:
        print(r)

a = "AABCAADAA"
merge(a)
