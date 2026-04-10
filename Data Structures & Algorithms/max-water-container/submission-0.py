class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_max = r_max = 0
        total = 0
        l = 0
        r = len(heights) -1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            total = max(total, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            # if heights[l] < heights[r]:
            #     if heights[l] >= l_max:
            #         l_max = heights[l]
            #     else:
            #         total += l_max - heights[l]
            #     l += 1
            # else:
            #     if heights[r] >= r_max:
            #         r_max = heights[r]
                    
            #     else:
            #         total += r_max -heights[r]
            #     r -= 1
            # print(l_max, r_max)
        # total = l_max * r_max
        return total