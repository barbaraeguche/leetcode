# name: 20. valid parentheses
# link: https://leetcode.com/problems/valid-parentheses

# solution #
class Solution:
  def isValid(self, s: str) -> bool:
    open, closed = "({[", ")}]"
    stack = []
    
    def isEmpty(stack: List[str]) -> bool:
      return not bool(stack)

    for brac in s:
      if brac in open:
        stack.append(brac)
      elif brac in closed:
        if isEmpty(stack):
          return False

        ob = stack.pop()
        if brac != closed[open.index(ob)]:
          return False

    return isEmpty(stack)
