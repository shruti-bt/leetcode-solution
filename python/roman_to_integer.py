"""
Link to the problem: https://leetcode.com/problems/roman-to-integer/

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

"""



class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        out = 0
        for i in range(len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                out = out - dict[s[i]]
            else:
                out = out + dict[s[i]]  
        out = out + dict[s[-1]]
        return out

if __name__ == "__main__":
    s = "LVIII"
    soluction = Solution()
    print(soluction.romanToInt(s))