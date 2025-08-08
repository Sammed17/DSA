class Solution(object):
    def reverse(self, x):
        
        sign = -1 if x < 0 else 1
        num = abs(x)            
        result = 0

        while num > 0:
            last_digit = num % 10
            num = num // 10

            if result > (2**31 -1)//10:
                return 0
            result = result * 10 + last_digit 

        return sign * result
