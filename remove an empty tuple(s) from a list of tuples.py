l=[(123,345,666),(777,5555,666),()]
for i in l:
    if i==():
        l.remove(i)
print(l)