def solution(nums, x):
    nums.sort()
    ops = 0

    for i in range(len(nums)//2):
        ops += max(nums[i]-x, 0)
    
    ops += abs(nums[len(nums)//2]-x)

    for i in range((len(nums)//2)+1, len(nums)):
        ops += max(x-nums[i], 0)

    return ops

print(solution([6, 5, 8], 8))
print(solution([1, 4, 7, 12, 3, 5, 9], 5))

# sort the input array
# loop on left half of array (excluding middle) and calculate number of operations necessary to make each number <= median
# for middle value, calculate number of operations necessary to make it = median
# for right half of array (excluding middle) calculate number of operations necessary to make each number >= median
# return total count of operations done