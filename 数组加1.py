##给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#你可以假设除了整数 0 之外，这个整数不会以零开头。


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):   #非常棒!说明从python的最后一位开始!
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return digits

if __name__ == '__main__':
    so =Solution()
    b = [1,1,3,9]
    a = so.plusOne(b)
    print(a)
