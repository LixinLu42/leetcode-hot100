class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1
        # if len(s) %2 ==1:
        #     return False
        # stack = list()
        # pair = {
        #     ")":"(",
        #     "}":"{",
        #     "]":"["
        #     }

        # for c in s:
        #     if c in pair:
        #         if (not stack) or (stack[-1] != pair[c]):
        #             return False
        #         stack.pop()

        #     else:
        #         stack.append(c)

        # return not stack

        # 2
        if len(s) %2 ==1:
            return False
        stack = list()

        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] == '[' and c == ']':
                stack.pop()
            elif stack[-1] == '{' and c == '}':
                stack.pop()
            elif stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)
        return not stack

s = "({[)"
a = Solution()
print(a.isValid(s))