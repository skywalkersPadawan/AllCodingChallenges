# Definition for a binary tree node.
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while stack:
            # this is to print stack and res
            currentValue = stack.pop()
            if type(currentValue) != int and currentValue:
                if currentValue.left:
                    stack.append(currentValue.right)
                    stack.append(currentValue.val)
                    stack.append(currentValue.left)
                elif currentValue.right:
                    stack.append(currentValue.right)
                    stack.append(currentValue.val)
                    stack.append(currentValue.left)
                else:
                    result.append(currentValue.val)
            elif currentValue != None:
                result.append(currentValue)

        return result
