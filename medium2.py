def majorityElement(nums):
    count1, count2, candidate1, candidate2 = 0, 0, None, None

    # Finding candidates for potential majority elements
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Counting occurrences of the potential majority elements
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

# Test cases
nums1 = [3, 2, 3]
print("Output for [3, 2, 3]:", majorityElement(nums1))

nums2 = [1]
print("Output for [1]:", majorityElement(nums2))

nums3 = [1, 2]
print("Output for [1, 2]:", majorityElement(nums3))
