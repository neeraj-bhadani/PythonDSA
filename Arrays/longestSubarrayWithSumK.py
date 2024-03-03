class Solution:

    def longestsubarray(self, a, K):
        """brute"""
        max_length = 0
        for i in range(0, len(a)):
            _sum = 0
            for j in range(i, len(a)):
                _sum = _sum + a[j] 
                if _sum == K:
                    max_length = max(max_length, j - i + 1)

        return max_length
    
    def longestSubArrayK2(self, arr, k):
        """better for positives, best for arrays having both positives and negatives"""
        cum_sum = 0
        # hashmap = {}
        hashmap = {0:-1}
        max_len = -1
        #  initialization se 0th index element hit scenario cover ho raha hai, otherwise use below comment code

        for i in range(len(arr)):
            print("i->", i)
            cum_sum = cum_sum + arr[i]
            # if cum_sum == k:
            #     max_len = max(max_len, i+1)
            if cum_sum-k in hashmap:
                max_len = max(max_len, i-hashmap[cum_sum-k])
            if cum_sum not in hashmap:
                hashmap[cum_sum] = i
            print(max_len)

        return max_len
    
    def longestSubArrayK3(self,arr, k):
        """best for positives, can't do with zeroes or negatives"""
        l = r = 0
        cum_sum = arr[0]
        max_len = 0
        while(r<len(arr)):
            while(cum_sum>k and l<=r):
                cum_sum -= arr[l]
                l+=1
            if cum_sum == k:
                max_len = max(max_len, r-l+1)
            r+=1
            if r<len(arr):
                cum_sum += arr[r]
        return max_len


if __name__ == '__main__':
    K = int(input())
    arr = list(map(int, input().strip().split()))
    print(Solution().longestSubArrayK3(arr, K))

