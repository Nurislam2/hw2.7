import random
def binary_serch(key,list):
    left=0
    right=len(list)-1
    while left<=right:
        mid=(left+right)//2
        if list[mid]==key:
            print(f"элемент найден \nЕго индекс {mid}")
            break
        elif list[mid]>key:
            right=mid-1
        else:
            left=mid+1
a=[1,2,3,4,5,6,7,8,9,10]
binary_serch(4,a)

def buble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=a[j+1]
                arr[j+1]=temp

arr=[]
for i in range(0,10):
    arr.append(random.randint(0,20))
buble_sort(arr)
print(arr)
