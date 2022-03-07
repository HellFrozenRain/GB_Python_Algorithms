# 117. Populating Next Right Pointers in Each Node II
"""Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL."""

from collections import deque


class Solution:
    def connect(self, root):
        if not root:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            current = None
            nxt = None

            for i in range(len(queue)):
                if not current:
                    current = queue.popleft()
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                elif not nxt:
                    nxt = queue.popleft()
                    current.next = nxt
                    if nxt.left:
                        queue.append(nxt.left)
                    if nxt.right:
                        queue.append(nxt.right)
                else:
                    current = queue.popleft()
                    nxt.next = current
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                    nxt = current

        return root
