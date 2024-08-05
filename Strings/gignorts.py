s = 'Sorting1234'
upper = ''.join([n for n in s if n.isupper()])
lower = ''.join([n for n in s if n.islower()])
number = [int(n) for n in s if n.isdigit()]
odd = [n for n in number if n % 2 != 0]
even = [n for n in number if n % 2 == 0]
arr = [str(item) for sublist in [sorted(lower), sorted(upper),sorted(odd),sorted(even)] for item in sublist]
print("".join(arr))
