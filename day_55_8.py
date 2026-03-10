#array findging duplicate using sorting 

def find_duplicate(nums):
    nums.sort()
    
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return nums[i]

nums = [1,3,4,2,2]
print(find_duplicate(nums))