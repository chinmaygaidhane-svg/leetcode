class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[]
        for i in nums:
            if i!=0:
                a.append(i)

        for i in nums:
            if i==0:
                a.append(i)

        for i in range(len(nums)):
            nums[i] = a[i]

        
                