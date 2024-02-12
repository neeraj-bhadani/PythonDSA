class Solution:
    def unionoftwosortedarrays(self, a, b):
        # simple approach
        c = set(a+b)
        c = list(c)
        return c
    
    def union2(self, a , b):
        n1 = len(a)
        n2 = len(b)
        # two pointer approach
        i = j = 0
        unionarr = []
        while(i<n1 and j<n2):
            if a[i] <= b[j]:
                if a[i] not in unionarr:
                    unionarr.append(a[i])
                i = i+1
            
            elif a[i] > b[j]:
                if b[j] not in unionarr:
                    unionarr.append(b[j])
                j = j+1

        while(i<n1):
            if a[i] not in unionarr:
                unionarr.append(a[i])
            i = i+1
        
        while(j<n2):
            if b[j] not in unionarr:
                unionarr.append(b[j])
            j = j+1

        return unionarr


if __name__ == '__main__':
    arr2 = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))

    print(Solution().union2(arr, arr2))