#to find the maximum sum of the subarray
def max_subarray_sum(nums):
    if nums is None:
        return 0
    current_max=global_max=nums[0]
    for i in range(1,len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        if current_max>global_max:
            global_max=current_max
    return global_max

arr=[2,-3,2,-7,1,-1,6,12,6]
print(max_subarray_sum(arr))