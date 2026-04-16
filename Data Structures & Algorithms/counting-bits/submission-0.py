class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            arr.append(i)
        print(arr)
        bin_arr = []
        for i in arr:
            val = bin(i)[2:]
            bin_arr.append(val)
        print(bin_arr)
        output = []
        for i in bin_arr:
            val = i.count('1')
            output.append(val)
        return output
        