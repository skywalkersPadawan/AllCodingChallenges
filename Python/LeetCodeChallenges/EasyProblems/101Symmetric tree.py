# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(numberOne, numberTwo):
            if not numberOne and not numberTwo:
                return True
            if (not numberOne and numberTwo) or (not numberTwo and numberOne):
                return False

            return (
                numberOne.val == numberTwo.val
                and symmetric(numberOne.left, numberTwo.right)
                and symmetric(numberOne.right, numberTwo.left)
            )

        return symmetric(root, root)
