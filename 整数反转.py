# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# python代码实现，基本的思路是，首先将判断输入x的符号，有正、负和0。
# 处理0时，直接定义为0：num_sum = 0。处理正负时，将数据转化为正数，
# 其中flag作为符号。翻转的思路是:依次取数据的个位数(x%10),然后将其整除10(x//10)。
# 逐步减小数据直到为0，list保存数据，有效的解决个位数为0情况。
# 来源：力扣（LeetCode）
# 注意:假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。

class Solution:
    def reverse(self, x) :
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        num_list = []

        while x:
            num_list.append(x%10)   #这步很重要!!!
            x = x//10
        num_sum = 0

        num_len = len(num_list)
        for i,item in enumerate(num_list):
            #enumerate()(单词意思是枚举的意思)是python中的内置函数
            #函数中的参数num_list可以是一个迭代器(iterator)或者是一个序列.
            #enumerate与range相对
            num_sum += item * 10 ** (num_len-i-1)
        num_sum = flag*num_sum
        if (num_sum < - 2**31 ) or  (num_sum >  2**31 - 1 ):
            return 0
        else:
            return num_sum

if __name__ == '__main__':
    so =Solution()   # 创建对象时，只需使用类名，且类名后面要带括号！
    a = so.reverse(4673) #然后使用创建的对象调用该类的方法，并把调用该方法得到的结果赋值给变量ss
    print(a)


    '''
        ***星号情况
        调用函数时，两个**的情况：
        
        和上面3.1.2很像，是分配字典的。
        
        这回params是一个字典了：
        
        params={'x':1,'y':2}
        
        可以通过如下方式调用myprint函数：
        
        >>> myprint(**params)
        
        就可以输出：
        
            1
            2
    '''
