class Solution:
    def CheckAlpha(self,number):
        result=""
        while number>0:
            number-=1
            remainder=number%26
            result=chr(remainder+ord('A')) + result
            number //=26
        return result
solution=Solution()
columnNumber = 701
result=solution.CheckAlpha(columnNumber)
print(result)