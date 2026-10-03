class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = []
        count = 0

        for i in nums:
            if i not in a:
                a.append(i)
                count += 1

        for i in range(count):
            nums[i] = a[i]

        return count