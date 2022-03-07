"""Given a binary tree, find the lowest common ancestor (LCA)
 of two given nodes in the tree."""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None

        def dfs(root):
            nonlocal result

            if not root:
                return False, False

            left_p, left_q = dfs(root.left)
            right_p, right_q = dfs(root.right)

            found_p = root == p or left_p or right_p
            found_q = root == q or left_q or right_q

            if found_p and found_q and not result:
                result = root

            return found_p, found_q

        dfs(root)
        return result
