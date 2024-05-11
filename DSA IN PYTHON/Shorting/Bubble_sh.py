def bubble_short(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1] = data_list[i+1],data_list[i]


def modife_bubble_short(data_list):
    flags = False
    for r in range(1,len(data_list)):
        flags = False
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1] = data_list[i+1],data_list[i]
                flags = True
            if not flags:
                break



l = [90,65,32,76,43,23]
# bubble_short(l)
modife_bubble_short(l)
print(l)