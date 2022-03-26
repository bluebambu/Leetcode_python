from XiangUtils.xiangUtils import Tree


# score: 97.89
class Solution:
    def simplifyPath2(self, path: str) -> str:
        elem = path.split('/')
        skipCnt = 0
        res = []
        for e in reversed(elem):
            if e == '..':
                skipCnt += 1
            elif e == '.' or e == '':
                pass
            else:
                if skipCnt > 0:
                    skipCnt -= 1
                else:
                    res.append(e)

        return '/' if not res else '/'+'/'.join(reversed(res))

    def simplifyPath(self, path: str) -> str:
        

tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.simplifyPath("/home/")
print(r)
r = s.simplifyPath("/../")
print(r)
r = s.simplifyPath("/a/b/.//../../c/")
print(r)
r = s.simplifyPath("/home")
print(r)
