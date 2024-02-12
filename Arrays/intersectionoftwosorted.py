class Solution:
    def intersect(self, a , b):
        n1 = len(a)
        n2 = len(b)
        # two pointer approach
        i = j = 0
        intersectarr = []
        while(i<n1 and j<n2):
            if a[i] < b[j]:
                i = i+1
            elif a[i] > b[j]:
                j = j+1
            else:
                intersectarr.append(a[i])
                i = i+1
                j = j+1
                
        return intersectarr


if __name__ == '__main__':
    arr2 = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))

    print(Solution().intersect(arr, arr2))