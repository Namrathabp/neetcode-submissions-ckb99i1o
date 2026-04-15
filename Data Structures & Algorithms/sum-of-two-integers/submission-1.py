class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a = format(a, 'b')
        # b = format(b, 'b')
        # a = bin(a)[2:]
        # b = bin(b)[2:]
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b)& mask
            b = carry << 1
        return a if a <= 0x7FFFFFFF else ~(a^mask)
             