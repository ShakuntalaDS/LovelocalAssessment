from collections import deque
# sliding window problem
def maxSlidingWindow(nums, k):
    if not nums:
        return []

    if k == 1:
        return nums

    max_window = []
    window = deque()

    for i, num in enumerate(nums):
        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        if window[0] == i - k:
            window.popleft()

        if i >= k - 1:
            max_window.append(nums[window[0]])

    return max_window

# Test cases
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
print("Input:", nums1, "k =", k1)
print("Output:", maxSlidingWindow(nums1, k1))

nums2 = [1]
k2 = 1
print("\nInput:", nums2, "k =", k2)
print("Output:", maxSlidingWindow(nums2, k2))
