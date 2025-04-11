# name: 20. valid parentheses
# link: https://leetcode.com/problems/valid-parentheses

# solution #
class Solution:
  def isValid(self, s: str) -> bool:
    open_brac = "({["
    closed_brac = ")}]"
    stack = []

    for brac in s:
      if brac in open_brac:
        stack.append(brac)
      elif brac in closed_brac:
        if self.is_empty(stack):
          return False

        ob = stack.pop()
        if brac != closed_brac[open_brac.index(ob)]:
          return False

    return self.is_empty(stack)
        
  @staticmethod
  def is_empty(stack: List[str]) -> bool:
    return not bool(stack)
