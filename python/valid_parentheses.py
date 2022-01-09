"""
Link to the problem: https://leetcode.com/problems/valid-parentheses/

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brac = ['(', '[', '{']
        for current_brac in s:
            if current_brac in open_brac:
                stack.append(current_brac)
            else:
                last_open_brac = stack.pop()
                if last_open_brac == "(":
                    if current_brac != ")": return "false"
                if last_open_brac == "[":
                    if current_brac != "]": return "false"
                if last_open_brac == "{":
                    if current_brac != "}": return "false"
                
        if len(stack) == 0: 
            return "true"
        else:
            return "false"

if __name__ == "__main__":
    s = "()[]{}"
    soluction = Solution()
    print(soluction.isValid(s))
        
        
        