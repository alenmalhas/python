'''
Solution: Search Suggestions System

Leetcode Problem #1268 (Medium): Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/
solution:
https://dev.to/seanpgallivan/solution-search-suggestions-system-90e


UBS: search suggestion question; sample word: camera
	
Leetcode 1268. Search Suggestions System ( Java / Javascript / C#)
https://thechanmoon.medium.com/leetcode-1268-search-suggestions-system-java-javascript-53a30cf69564

Solution: Search Suggestions System
https://dev.to/seanpgallivan/solution-search-suggestions-system-90e

Leetcode Solutions Index
https://dev.to/seanpgallivan/leetcode-solutions-index-57fl


Example 1:	
Input:	products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output:	[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation:	
    products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]


Example 2:	
Input:	products = ["havana"], searchWord = "havana"
Output:	[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:	
Input:	products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output:	[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:	
Input:	products = ["havana"], searchWord = "tatiana"
Output:	[[],[],[],[],[],[],[]]

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