##https://leetcode-cn.com/problems/pascals-triangle/solution/yang-hui-san-jiao-by-leetcode/
##给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        ##其中’_’ 是一个循环标志，也可以用i，j 等其他字母代替，
        ##下面的循环中不会用到，起到的是循环此数的作用
        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            #就是直接把row上所有的位置都变成None,
            #然后在下一句：row[0], row[-1] = 1,
            #1将首末位变成已知的值1。之后在下边的操作计算中间的值。
            row[0], row[-1] = 1, 1   #设置首项和末项
            #print(row)

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):  #去掉首末
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
                print(row)

            triangle.append(row)
        return triangle

if __name__ == '__main__':
    so = Solution()
    a = so.generate(6)
    print(a)

##1.通过观察杨辉三角的数字规律可以确定一些位置的值，每一行的首位和末尾都是1。
##2.首先定义一个目标数组（最后返回的结果），之前也做过一个将临时数组添加到目标数组的题目（可以看一下第二十三天的内容）。
##3.开始循环，在循环中定义了一个数组row，这个row在第一次for循环时，row=[None]，然后row[0]=1改变了row=[None]，进入第二个for循环，这个j代表的索引就是row数组中非1的那些位置（除首末以外的中间位置）。
##4.这个时候找到当前行的前一行数组再找到该数组j索引的前一个索引上的值（也就是每个数的左上方的值），同理找到这个元素右上方的值，两个值之和赋值给row的j索引，主要操作就完成了。
##5.row放入triangle中，进行下一次循环操作，循环完毕后，返回triangle数组，就可以得到杨辉三角啦。
##6.对于这句的理解：row = [None for i in range(row_num+1)]，就是直接把row上所有的位置都变成None,然后在下一句：row[0], row[-1] = 1, 1将首末位变成已知的值1。之后在下边的操作计算中间的值。
