#给你两个二进制字符串，返回它们的和（用二进制表示）。
#输入为 非空 字符串且只包含数字 1 和 0。
#对于python的数组和字符非常有用!!

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a==b=='0':
            return 0
        num1=num2=0
        for i,x in enumerate(a):
            num1+=int(x)*(2**(len(a)-i-1))
        for i,x in enumerate(b):
            num2+=int(x)*(2**(len(b)-i-1))
        num=num1+num2
        print(num)
        numss=""
        while num>0:
            nums=num%2  #取余
            numss+=str(nums)  #字符相加
            num=num//2   #两个除号就是向下取整
            print(num)
        print(numss)
        return numss[::-1]

if __name__ == '__main__':
    so = Solution()
    a = '1010'
    b = '11'
    c = so.addBinary(a,b)
    print(c)

    #或者用python的内置函数:
    #return bin(int(a,2)+int(b,2))[2:]

