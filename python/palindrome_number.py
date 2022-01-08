"""
Link to the problem: https://leetcode.com/problems/palindrome-number/

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        while x > 0:
            remainder = x % 10
            rev = rev * 10 + remainder
            x = x // 10
            
        if temp == rev:
            return True
        else:
            return False

if __name__ == "__main__":
    x = 121
    soluction = Solution()
    print(soluction.isPalindrome(x))
            
