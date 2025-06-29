import time

def time_dec(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=end-start
        print(f"time for running {func.__name__} is {total_time:.6f}")
        return result
    return wrapper


def qsort(my_list):
    if len(my_list)<=1:
        return my_list
    left=[]
    right=[]
    middle=[]
    pivot=my_list[len(my_list)//2]
    for item in my_list:
        if item<pivot:
            left.append(item)
        if item==pivot:
            middle.append(item)
        if item>pivot:
            right.append(item)
    return qsort(left)+middle+qsort(right)

def bsort(my_lsit):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[i]<my_list[j]:
                my_list[i],my_list[j]=my_list[j],my_list[i]
    return my_list


def msort(my_list):
    if len(my_list)<=1:
        return my_list
    mid=len(my_list)//2
    left=msort(my_list[:mid])
    right=msort(my_list[mid:])
    return merge(left,right)

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



my_list=[12,43,12,5,6,57,45,85,12,64,43,63,34,65,7,687,9,7,9,97,65,6,56,4,535,25,234,235,16,86]
@time_dec  
def run_qsort(my_list):
    sort_list=qsort(my_list)
    print(f"quick sort : {sort_list}")
run_qsort(my_list)

@time_dec
def run_bsort(my_list):
    sort_list=bsort(my_list)
    print(f"bubble sort : {sort_list}")
run_bsort(my_list)

@time_dec
def run_msort(my_list):
    sort_list=msort(my_list)
    print(f"merge sort : {sort_list}")
run_msort(my_list)