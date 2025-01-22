# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str):

        start = 0
        answer = 0
        hash_dict = {}

        for i in range(len(s)):
            
            if s[i] in hash_dict:
                start = max(start, hash_dict[s[i]] + 1)

            hash_dict[s[i]] = i
            answer = max(answer, i - start + 1)
        
        return answer