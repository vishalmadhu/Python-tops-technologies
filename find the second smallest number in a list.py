def second_small(list):
    smallest=list[0]
    second_smallest=list[0]
    for i in list:
        if i<smallest:
            second_smallest=smallest
            smallest=i
        elif i<second_smallest and i!= smallest:
            second_smallest=i
    print(second_smallest)

list=[2,3,4,5,6,7,4,0,1]
second_small(list)
