dic={'a':1,'b':2,'c':3}
dic1={'d':4,'e':5}
dic2={'f':6,'g':7}
dic3={}
for i in (dic,dic1,dic2):
    dic3.update(i)
print(dic3)