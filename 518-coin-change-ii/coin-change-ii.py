class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n=len(coins)
        @lru_cache(None)
        def find(ind,amount):
            if amount==0:
                return 1
            if ind==0:
                return 1 if amount%coins[ind]==0 else 0
            not_take=find(ind-1,amount)
            take=0
            if coins[ind]<=amount:
                take=find(ind,amount-coins[ind])
            return take+not_take
        ans=find(n-1,amount)
        return ans
        
