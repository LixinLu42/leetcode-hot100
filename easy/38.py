# 1. two while
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if(1 == n):
#             return '1'  
#         if(0 == n):
#             return ''
        
        
#         i = 1
#         s = '1'

#         while(i <= n):
#             k = 0
#             a = s[k]
#             res = ''
#             count = 0
#             while(k < len(s)):
#                 if(a == s[k]):
#                     count += 1
#                     k += 1
#                     continue
#                 res = res + str(count) + a
#                 count = 0
#                 a = s[k]
#             res = res + str(count) + a
            
            
#             s = res
#             i += 1
#         return s


# iter
class Solution:
    def countAndSay(self, n: int) -> str:
        if(1 == n):
            return '1'  
        if(0 == n):
            return ''
        
        s = '1'
        res = ''
        count = 1

        return self.iter(s, res, count, n)


    def iter(self, s, res, count, n):
        if count == n:
            return s

        index = 0
        k = 0
        a = s[k]
        while(k < len(s)):
            if a == s[k]:
                k += 1
                index += 1
                continue
            res = res + str(index) + a
            a = s[k]
            index = 0
        res = res + str(index) + a 
        s = res
        res = ''
        return self.iter(s, res, count+1, n)


output = ''
a = Solution()
output = a.countAndSay(4)
print(output)
