from XiangUtils.xiangUtils import TreeNode, Tree

found = False
next = None

# score: 13%
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        found = False
        next = None

        def dfs(node, p):
            nonlocal found
            nonlocal next
            if not node:
                return
            dfs(node.left, p)
            if node is p:
                found = True
            if node is not p and found:
                next = node
                found = False
            dfs(node.right, p)

        dfs(root, p)
        return next


# 13%
class Solution2:
    def inorderSuccessor(self, root: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        p = root
        prev = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            cur = stack.pop()
            if prev is q:
                return cur

            prev = cur
            if cur.right:
                p = cur.right

        return None

# 40%
class Solution3:
    def inorderSuccessor(self, root: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p = root
        res = None
        while p:
            if p.val > q.val:
                res = p
                p = p.left
            else:
                p = p.right
        return res




tree = Tree('2,1,#,#,#')
s = Solution2()
r = s.inorderSuccessor(tree.root, tree.root)
print(r.val)

tree = Tree('2,1,3,#,#,#,#')
s = Solution2()
r = s.inorderSuccessor(tree.root, tree.root.left)
print(r.val)

