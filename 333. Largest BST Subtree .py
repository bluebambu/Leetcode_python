from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder

# score: 23%
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        maxsz = 0
        res = None

        def isBstAndCnt(node: TreeNode):
            if not node:
                return True, None, 0
            lis, lrng, lsz = isBstAndCnt(node.left)
            ris, rrng, rsz = isBstAndCnt(node.right)
            if (not lis) or (not ris):
                return False, None, 0

            v = node.val
            if (lrng and v <= lrng[1]) or (rrng and v >= rrng[0]):
                return False, None, 0
            cursz = lsz + rsz + 1
            nonlocal maxsz
            nonlocal res
            if cursz > maxsz:
                maxsz = cursz
                res = node
            lb = lrng[0] if lrng else v
            rb = rrng[0] if rrng else v
            return True, [lb, rb], cursz

        isBstAndCnt(root)
        return maxsz



tree = Tree('10,5,15,1,8,#,7,#,#,#,#,#,#')
lvlOrder(tree.root)
s = Solution()
r = s.largestBSTSubtree(tree.root)
print(r)

tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
lvlOrder(tree.root)
s = Solution()
r = s.largestBSTSubtree(tree.root)
print(r)
