#finding max number 

def find_max(nums):
    max_num = nums[0]

    for num in nums:
        if num > max_num:
           max_num = num

    return max_num


nums = [3,4,5,78,98,444]
print(find_max(nums))
