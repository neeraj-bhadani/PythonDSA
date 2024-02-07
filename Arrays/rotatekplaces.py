import sys

class Solution:
    def rotatebyk(self, a, n, k):
        temp1 = (a[0:k][::-1] + a[k:n][::-1])[::-1]
        return temp1

if __name__ == '__main__':
    size = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    print(Solution().rotatebyk(arr, size, k))
