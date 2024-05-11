
def bubble_sort(data_list):
    n = len(data_list)
    for r in range(1,n):
        for i in range(n-r):
            if data_list[i] > data_list[i+1]:
                data_list[i],data_list[i+1] = data_list[i+1],data_list[i]


def selection_sort(data_list):
   n = len(data_list)
   for i in range(n-1):
       mini  = i
       for j in range(i+1,n):
           if data_list[j] < data_list[mini]:
               mini = j
       data_list[i],data_list[mini] = data_list[mini],data_list[i]
       
       
def insertion_sort(data_list):
    n = len(data_list)
    for i in range(1,n):
        key = i
        j = i + 1
        while j >= 0 and key < data_list[j]:
            data_list[j+1] = data_list[j]
            j -= 1
        data_list[j+1] = data_list[key]


l = [23,45,32,87,23,64,9]
# bubble_sort(l)
selection_sort(l) 
print(l)