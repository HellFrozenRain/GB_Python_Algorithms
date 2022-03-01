"""Проверить дерево на симметричность"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_mirror(root):
    return check_halves(root.left, root.right)


def check_halves(left, right):
    if not left and not right:
        return True
    if left and right:
        if left.data == right.data:
            left_half = check_halves(left.left, right.right)
            right_half = check_halves(left.right, right.left)
            return left_half and right_half
    return False


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(3)
tree1.right.right = TreeNode(3)
tree1.left.right = TreeNode(4)
tree1.right.left = TreeNode(4)


print(is_mirror(tree1))

# leetcode
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
#
#         return self.is_mirror(root.left, root.right)
#
#     def is_mirror(self, leftroot, rightroot):
#         if leftroot and rightroot:
#             return (leftroot.val == rightroot.val and
#                     self.is_mirror(leftroot.left, rightroot.right) and
#                     self.is_mirror(leftroot.right, rightroot.left))
#         return leftroot == rightroot
