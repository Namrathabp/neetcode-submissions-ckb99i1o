class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetFreq = {}
        for c in t:
            targetFreq[c] = targetFreq.get(c, 0)+1
            required = len(targetFreq)
            left = 0
            right = 0
            formed = 0
            windowFreq = {}
            minLen = float('inf')
            minLeft = 0
            while right < len(s):
                c = s[right]
                windowFreq[c] = windowFreq.get(c, 0) + 1
                if c in targetFreq and windowFreq[c] == targetFreq[c]:
                    formed += 1
                while left <= right and formed == required:
                    if right - left + 1 < minLen:
                        minLen = right - left + 1
                        minLeft = left
                    leftchar = s[left]
                    windowFreq[leftchar] -= 1

                    if leftchar in targetFreq and windowFreq[leftchar] < targetFreq[leftchar]:
                        formed -= 1
                    
                    left += 1
                right += 1
        return "" if minLen == float('inf') else s[minLeft:minLeft+minLen]

        
    # def containsAll(self, windowFreq, targetFreq):
    #     for char in targetFreq:
    #         if windowFreq.get(char, 0) < targetFreq[char]:
    #             return False
    #         return True
        