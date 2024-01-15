import sys

class Solution:
    def thirdLargest(self, a, n):
        if n < 3:
            return -1
        else:
            first = second = third = -sys.maxsize
            for i in range(0, n):
                if a[i] > first:
                    third = second
                    second = first
                    first = a[i]
                elif a[i] > second and a[i] != first:  # Added condition to handle duplicate elements
                    third = second
                    second = a[i]
                elif a[i] > third and a[i] != second:  # Added condition to handle duplicate elements
                    third = a[i]

            if third == -sys.maxsize:
                print("There is no third largest element.")
            else:
                return third
                    

if __name__ == '__main__':
    size = int(input())
    arr = list(map(int, input().strip().split()))
    print(Solution().thirdLargest(arr, size))
