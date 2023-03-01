def same (list1,list2):
    for i in list1:
        for j in list2:
            if  i==j:
                return True
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
print(same(list1,list2))