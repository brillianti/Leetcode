'''
    给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
    如果不存在最后一个单词，请返回 0 。
    说明：一个单词是指仅由字母组成、不包含任何空格字符的最大子字符串。
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/length-of-last-word
'''

class Solution:
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        count = 0
        flag = 0
        for i in s[::-1]:
            #使用的方式为:[起始位置,结束位置,步长]
            #那么a[::]及a[:]都代表着所有元素,使用默认元素,a=[1,2,3,4,5] 则a[0:len(a):1]
            #而a[::-1]代表着步长最负数,则为从序列的最后一个元素开始切片
            if i is " " and flag == 0:
                continue
            if i is not " ":
                count += 1
                flag = 1
            else:
                break
        return count

if __name__ == '__main__':
    So = Solution()
    c = So.lengthOfLastWord('hello  world')
    print(c)
