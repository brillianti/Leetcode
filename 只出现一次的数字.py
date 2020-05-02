#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#说明：
#你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/single-number
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

if __name__ == '__main__':
    so = Solution()
    b = [2,2,1]
    a = so.singleNumber(b)
    print(a)
