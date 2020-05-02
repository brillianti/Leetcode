#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#说明：
#你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/single-number-ii

#解题思路
#将输入数组存储到 HashSet，然后使用 HashSet 中数字和的三倍与数组之和比较。
#3×(a+b+c)−(a+a+a+b+b+b+c)=2c3 \times (a+b+c)-(a+a+a+b+b+b+c)=3×(a+b+c)−(a+a+a+b+b+b+c)=2c
class Solution:
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2

if __name__ == '__main__':
    so = Solution()
    b = [1,2,1,1]
    a = so.singleNumber(b)
    print(a)



