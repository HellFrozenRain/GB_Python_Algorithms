"""Реализовать обход дерева post-order. Сначала левое, потом правое поддерево,
в последнюю очередь корень"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        self.result = []

        def post_order(node):
            if node == None:
                return None

            post_order(node.left)
            post_order(node.right)
            self.result.append(node.val)

        post_order(root)

        return self.result

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

print(Solution.postorderTraversal(Solution, tree))
"""Итеративно"""
# class Solution:
#     def postorderTraversal(self, root: [TreeNode]) -> [int]:
#         stack = []
#         result = []
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             temp = stack[-1].right
#             if temp:
#                 root = temp
#             else:
#                 temp = stack.pop()
#                 result.append(temp.val)
#                 while stack and temp == stack[-1].right:
#                     temp = stack.pop()
#                     result.append(temp.val)
#         return result
# Definition for a binary tree node.
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#
#
"""Рекурсивно"""
# def printPostorder(root):
#     if root:
#         # First recur on left child
#         printPostorder(root.left)
#
#         # the recur on right child
#         printPostorder(root.right)
#
#         # now print the data of node
#         print(root.val)
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# # print nPostorder traversal of binary tree is"
# printPostorder(root)
