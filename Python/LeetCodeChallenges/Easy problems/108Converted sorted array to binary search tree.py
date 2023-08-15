# Definition for a binary tree node.
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, numbers: List[int]) -> Optional[TreeNode]:
        if not numbers:
            return None
        midNumber = len(numbers) // 2
        node = TreeNode(numbers[midNumber])
        node.left = self.sortedArrayToBST(numbers[:midNumber])
        node.right = self.sortedArrayToBST(numbers[midNumber + 1 :])
        return node
