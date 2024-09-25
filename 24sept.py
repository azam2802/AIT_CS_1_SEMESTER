nums = [1,2,2,4,5,6]

def check_error(nums):
    for index, val in enumerate(nums):
        if index != len(nums)-1 and val == nums[index+1]:
            duplicate = val
            set1 = set(nums[:index+1])
            set2 = set(nums[index+1:]) 
    set3 = set1.intersection(set2)
    set3.add(duplicate+1)
    print(list(set3))

check_error(nums)
