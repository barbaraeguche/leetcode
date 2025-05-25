# name: 125. valid palindrome
# link: https://leetcode.com/problems/valid-palindrome

# solution #
class Solution:
  def isPalindrome(self, s: str) -> bool:
    alpha_num = ''.join(filter(str.isalnum, s)).lower()
    return alpha_num == alpha_num[::-1]
