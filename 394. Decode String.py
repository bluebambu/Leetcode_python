from XiangUtils.xiangUtils import Tree


# score: 5%
class Solution:
    def decodeString(self, s: str) -> str:
        r = ''
        i = 0
        while i<len(s):
            c = s[i]
            if c.isdigit():
                for j in range(i+1, len(s)):
                    if not s[j].isdigit():
                        break
                cnt = int(s[i:j])
                i = j+1

                lb = 0
                for j in range(j, len(s)):
                    if s[j] == '[':
                        lb += 1
                    if s[j] == ']':
                        lb -= 1
                    if lb == 0:
                        break

                content = s[i:j]
                r += cnt*self.decodeString(content)
                i = j+1
            else:
                r += c
                i += 1

        return r


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.decodeString('3[a]2[bc]')
print(r)
r = s.decodeString('3[a2[c]]')
print(r)
r = s.decodeString('2[abc]3[cd]ef')
print(r)
