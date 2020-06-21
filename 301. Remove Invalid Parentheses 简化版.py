from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> str:
        def strip(s:str):
            r = ''
            score = 0
            for c in s:
                if c == '(':
                    score += 1
                    r += '('
                elif c==')':
                    if score > 0:
                        score -= 1
                        r += ')'
                    else:
                        pass
                else:
                    r += c
            return r

        def swap(s:str):
            r = ''
            for c in reversed(s):
                if c == '(':
                    r += ')'
                elif c == ')':
                    r += '('
                else:
                    r += c
            return r

        s = strip(s)
        s = swap(s)
        s = strip(s)
        return swap(s)

s = Solution()
s1 = "((((())()"
r1 = s.removeInvalidParentheses(s1)
print(r1)
s1 = "(()))))))()"
r1 = s.removeInvalidParentheses(s1)
print(r1)
s1 = ")(((("
r1 = s.removeInvalidParentheses(s1)
print(r1)
s1 = "(a()a)))(((A"
r1 = s.removeInvalidParentheses(s1)
print(r1)
