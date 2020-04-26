#给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
#你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/merge-sorted-array


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of nums1.复制了一个空间一样的数组!!!!!
        nums1_copy = nums1[:m]
        nums1[:] = []    #把nums1清空,用nums1_copy代替nums1

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0  #定义指针
        #用双指针
        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        # if there are still elements to add
            if p1 < m:
                nums1[p1 + p2:] = nums1_copy[p1:]   #整个数组相加
            if p2 < n:
                nums1[p1 + p2:] = nums1_copy[p2:]
        return nums1

if __name__ == '__main__':
    so = Solution()
    nums1 = [0,1,3,5,2]
    nums2 = [3,4,2,6,0]
    a = so.merge(nums1,5,nums2,5)
    print(a)
