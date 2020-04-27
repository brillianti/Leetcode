class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        numbers = '1234567890'
        letters ='abcdefghijklnmopqrstuvwxyz'
        s=s.lower()  #s = s.lower() 全部转小写//  s= s.upper() 全部转大写
        res=''
        for i in s:
            if i in numbers or i in letters:   #选取数字或者字母
                res+=i
        mid=len(res)>>1
        for i in range(mid):
            if res[i]!=res[len(res)-1-i]:
                return False
        return True

if __name__ == '__main__':
    so = Solution()
    b = 'Hi this is a ,,,1221 a si siht ih'
    a =so.isPalindrome(b)
    print(a)
