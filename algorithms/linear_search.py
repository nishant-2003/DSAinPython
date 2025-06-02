def linear_search(arr, target, index=0):
    if index>=len(arr):
        return False
    if arr[index]==target:
        return True
    return linear_search(arr,target,index+1)


arr_len=int(input("Enter the length of array:\t"))
arr=[]
target=int(input("Enter the target:\t"))
index=int(input("Start searching from:\t"))
for i in range (0,arr_len):
    element=int(input(f"Enter the element of position {i}:\t"))
    arr.append(element)
ans=linear_search(arr,target,index)
print(ans)
