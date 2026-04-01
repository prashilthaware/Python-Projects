def insertion_sort(arry):
    for i in range(1,len(arry)):
        key =arry[i]
        j=i-1
        while j>=0 and arry[j]>key:
            arry[j+1]=arry[j]
            j-=1
        arry[j+1]=key
my_array=[9, 5, 1, 4, 3]
insertion_sort(my_array)
print(my_array)