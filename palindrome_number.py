class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_size = len(str(x))
        for i in range(x_size):
            if x_str[x_size-i-1] != x_str[i]:
                return False
        return True
        


#12321

#12345

