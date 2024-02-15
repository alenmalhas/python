'''
Solution: Search Suggestions System

Leetcode Problem #1268 (Medium): Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/
solution:
https://dev.to/seanpgallivan/solution-search-suggestions-system-90e


Leetcode Solutions Index
https://dev.to/seanpgallivan/leetcode-solutions-index-57fl
'''

class Solution:
    def suggestedProducts(self, P: List[str], S: str) -> List[List[str]]:
        P.sort()
        ans, left, right = [], 0, len(P) - 1
        for i in range(len(S)):
            c, res = S[i], []
            while left <= right and (len(P[left]) == i or P[left][i] < c): left += 1
            while left <= right and (len(P[right]) == i or P[right][i] > c): right -= 1
            for j in range(3):
                if left + j > right: break
                else: res.append(P[left+j])
            ans.append(res)
        return ans