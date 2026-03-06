# Two Sum Problem
def twoSum(nums, target):
    hashmap = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

nums =[11,12,13,14,13,32,1,332141,3,4341324]
target = 23
print(twoSum(nums,target))