import sys

class Solution:
    def pushZeroesToEnd(self, a, n):
        j = 0  # Initialize the position to swap non-zero elements

        # Traverse the array and move non-zero elements to the front
        for i in range(0, n):
            if a[i] != 0:
                a[i], a[j] = a[j], a[i]
                j = j + 1

        return a

if __name__ == '__main__':
    size = int(input())
    arr = list(map(int, input().strip().split()))
    print(Solution().pushZeroesToEnd(arr, size))
