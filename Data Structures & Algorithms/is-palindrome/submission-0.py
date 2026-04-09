class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        new_str = ""
        for i in s:
            if i.isalnum():
                new_str += i
        
        reverse_str = new_str[::-1]
        if new_str == reverse_str:
            return True
        return False
        