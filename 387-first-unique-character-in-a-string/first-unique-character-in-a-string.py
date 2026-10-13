class Solution(object):
    def firstUniqChar(self, s):
        seen = []
        
        for i in range(len(s)):
            char = s[i]
            
            # If not checked yet
            if char not in seen:
                seen.append(char)
                
                # If it occurs exactly once in the entire string, return this index
                if s.count(char) == 1:
                    return i
                    
        return -1