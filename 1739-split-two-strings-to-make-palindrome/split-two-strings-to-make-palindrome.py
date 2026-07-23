class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        
        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        if is_palindrome(a, 0, n-1) or is_palindrome(b, 0, n-1):
            return True
        
        left, right = 0, n - 1
        while left < right and a[left] == b[right]:
            left += 1
            right -= 1
        
        if left >= right:
            return True
        
        if is_palindrome(a, left, right) or is_palindrome(b, left, right):
            return True
        
        left, right = 0, n - 1
        while left < right and b[left] == a[right]:
            left += 1
            right -= 1
        
        if left >= right:
            return True
        
        if is_palindrome(b, left, right) or is_palindrome(a, left, right):
            return True
        
        return False