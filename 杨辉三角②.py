#给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
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


            triangle.append(row)
        return triangle[numRows-1]

if __name__ == '__main__':
    so = Solution()
    a = so.generate(4)
    print(a)
