def bubble_sort(data_list):
    n = len(data_list)
    flags = False
    for r in range(1,n):
        flags = False
        for i in range(n-r):
            if data_list[i] > data_list[i+1]:
                data_list[i],data_list[i+1] = data_list[i+1],data_list[i]
                flags = True
        if not flags:
            break
            

l = [11,45,35,87,43,1,32]
bubble_sort(l)
print(l)