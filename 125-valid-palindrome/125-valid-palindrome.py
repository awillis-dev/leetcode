class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        str = ""
        for c in s:
            if c.isalnum():
                str += c
                
        for i in str:
            str = str.lower()

        start, end = 0, len(str)-1
        while start < end:
            if str[start] == str[end]:
                start += 1
                end -= 1
            else:
                return False
        return True