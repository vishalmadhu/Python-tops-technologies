list=["Vishal","ajay","aashish","harsh","navin","madam"]
count=0
for i in list:
    if len(i)>2 and i[:1]==i[-1:]:
        count=count+1
print(count)