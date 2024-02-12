class Solution:
    def missingNumber(self, a, n):
        # simple approach
        for i in range(0, n-1):
            flag = 0
            for j in range(1, n):
                if j == a[i]:
                    flag = 1
                    break
            if flag == 0:
                return i
        
    
    def approach2hashing(self, a, n):
        hash = [0] * (n+1)
        for i in a:
            hash[i] = 1
        
        for i in range(1, n+1):
            if hash[i] == 0:
                return i

    # best approaches below     
    def approach3sumAP(self, a , n):
        total = n*(n+1)/2
        summ = sum(a)
        return int(total - summ)
    
    def approach4XOR(self, a ,n):
        xor1 = xor2 = 0
        for i in range(0, n-1):
            xor1 = xor1 ^ a[i]
            xor2 = xor2 ^ (i+1)
        xor2 = xor2 ^ n
        return xor1 ^ xor2

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().strip().split()))
    print(Solution().approach4XOR(arr, N))