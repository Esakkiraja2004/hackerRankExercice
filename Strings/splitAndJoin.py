def split(line):
    line = line.split(" ")
    return "-".join(line)
line = "hello all this is Raja"
print(split(line))