n=input("enter String: ")

d = {}
for s in n:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
print(d)


