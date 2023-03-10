"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
Example 1:
Input: x = 121
Output: true
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:
Input: x = -101
Output: false 
"""


def is_palindrome(x):
    if x < 0:
        return False

    x_str = str(x)
    return x_str == x_str[::-1]


print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))
print(is_palindrome(-101))
