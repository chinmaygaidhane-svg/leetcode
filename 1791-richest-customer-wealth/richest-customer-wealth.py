class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_sum = float('-inf')
        
        for sub in accounts:
            t = 0  # Reset for each customer
            for i in sub:
                t += i
            
            if t > max_sum:
                max_sum = t  # Single '=' for assignment
        
        return max_sum