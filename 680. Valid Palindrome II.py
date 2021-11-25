from XiangUtils.xiangUtils import Tree


# score: 8.35%
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not str or len(s) == 1:
            return True

        l, r = 0, len(s)-1
        return self.check(s, l, r, 1)

    def check(self, s, l, r, cnt):
        if l >= r:
            return True

        if s[l] == s[r]:
            return self.check(s, l+1, r-1, cnt)
        else:
            if cnt == 0:
                return False
            return self.check(s, l+1, r, cnt-1) or self.check(s, l, r-1, cnt-1)




tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.validPalindrome("abc")
print(r)
r = s.validPalindrome("aba")
print(r)
r = s.validPalindrome("abac")
print(r)
