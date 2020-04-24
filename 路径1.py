##这道题实在不会 留作纪念一下:
#来源:https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/



class Solution:
    def uniquePaths(self, m, n) :
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)] #????
        print(dp)
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                print(dp[i][j])
        return dp[-1][-1]   #最后一个数字

if __name__ == '__main__':
    so = Solution()
    a = so.uniquePaths(8,4)
    print(a)
