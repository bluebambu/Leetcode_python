from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder

# score:
class Solution:
    def preorder(self, root:TreeNode):
        stack = []
        p = root
        r = []
        while p or stack:
            while p:
                r.append(p.val)
                stack.append(p)
                p = p.left

            cur = stack.pop()
            if cur.right:
                p = cur.right
        print(r)

    def inorder(self, root: TreeNode):
        stack = []
        p  = root
        r = []
        while p or stack:
            while p:
                stack.append(p)
                p=p.left
            cur = stack.pop()
            r.append(cur.val)
            if cur.right:
                p=cur.right
        print(r)


    def postorder(self, root: TreeNode):
        stack = []
        p  = root
        r = []
        prev = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            cur = stack[-1]
            if prev is cur.right or None == cur.right:
                r.append(cur.val)
                prev = cur
                stack.pop()
            else:
                p = cur.right
        print(r)



        


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
lvlOrder(tree.root)
print()
s = Solution()
s.preorder(tree.root)
s.inorder(tree.root)
s.postorder(tree.root)
