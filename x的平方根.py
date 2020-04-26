#实现 int sqrt(int x) 函数。
#计算并返回 x 的平方根，其中 x 是非负整数。
#由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/sqrtx
#解析:当 x≥2x \ge 2x≥2 时，它的整数平方根一定小于 x/2x / 2x/2 且大于 0，
#即 0<a<x/20 < a < x / 20<a<x/2。由于 a 一定是整数，
#此问题可以转换成在有序整数集中寻找一个特定值，因此可以使用二分查找。

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right

if __name__ == '__main__':
    so = Solution()
    a = so.mySqrt(999)
    print(a)
