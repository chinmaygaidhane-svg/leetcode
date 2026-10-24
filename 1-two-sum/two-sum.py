class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted((num, i) for i, num in enumerate(nums))


        low = 0
        high = len(arr) - 1

        while low < high:
            sum_val = arr[low][0] + arr[high][0]

            if sum_val == target:
                return [arr[low][1], arr[high][1]]

            if sum_val < target:
                low += 1
            else:
                high -= 1

