class Solution:
    def getElement(self, a):
        xor = 0 
        for i in a:
            xor = xor ^ i
        return xor


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(Solution().getElement(arr))