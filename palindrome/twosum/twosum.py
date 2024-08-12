nums = [2, 7, 11, 15]
target = 26

def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] != nums[j]:
                return print([i, j])
                
            
twosum(nums, target)
