"""
Link to the problem: https://leetcode.com/problems/longest-common-prefix/

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        for i in range(len(strs[0])):
            result = []
            long_str = strs[0][:i+1] #strs[0][i=0]-f
            for j in range(len(strs)):
                if strs[j].startswith(long_str):
                    result.append(True)
                else:
                    result.append(False)
            # print(result)
            if not all(result):
                break
            else:
                out = long_str
                
        if out == "":
            return ""
        else:
            return out

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    soluction = Solution()
    print(soluction.longestCommonPrefix(strs))