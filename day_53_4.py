#reverse an array

def reverse_array(nums):
    reversed_list = []
    for i in range(len(nums)-1, -1 , -1 ):
        reversed_list.append(nums[i])
    return reversed_list    

nums = [11,12,13,14,15]

print(reverse_array(nums))
