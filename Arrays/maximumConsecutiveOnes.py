class Solution:
    def maxConOnes(self, a):
        max_count = 0
        count = 0
        for i in a:
            if i == 1:
                count = count +1
                max_count = max(count, max_count)
            else:
                count = 0
        return max_count


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(Solution().maxConOnes(arr))