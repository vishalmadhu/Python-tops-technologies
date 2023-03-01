list=[1,2,3,33,4,4,55,"vishal","vishal"]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print(list)
print(list1)
