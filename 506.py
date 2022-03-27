class Solution():
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_arr = sorted(score)[::-1]
        result_list = [ str(i) for i in range(1,len(score)+1)]
        result_list[0] = "Gold Medal"; result_list[1] = "Silver Medal"; result_list[2] = "Bronze Medal"
        mapped = dict(zip(sorted_arr, result_list))
        return [mapped[item] for item in score]


        
    
thing = Solution()
print(thing.findRelativeRanks([5,4,3,2,1]))
print(thing.findRelativeRanks([10,3,8,9,4]))