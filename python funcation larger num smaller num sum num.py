list=[1,2,3,4,5,6,7,8]
def sum_smallest_largest (list):
    largest=list[0]
    smallest=list[0]
    sum=0
    for i in list:
        sum=sum+i
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
    print('Largest :',largest)
    print("Smallest :",smallest)
    print("Sum :",sum)

sum_smallest_largest(list)
