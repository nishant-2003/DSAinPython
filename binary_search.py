def arr_partition(arr,target,start,end):
    if (start>end):
        return False
    mid=start+(end-start)//2
    if (arr[mid]==target):
        return True
    if(arr[mid]>target):
        return arr_partition(arr,target,start,mid-1)
    else:
        return arr_partition(arr,target,mid+1,end)


def binary_search(arr,target):
    return arr_partition(arr,target,0,len(arr)-1)


ans=binary_search([1,2,3,4,5,6,7,8],9)
print(ans)