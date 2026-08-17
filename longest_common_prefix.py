class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      common = strs[0] #flower
      strs_size = len(strs)

      for i in range(1, strs_size):
        res = ""
        for j in range(min(len(strs[i]), len(common))):
          if common[j] == strs[i][j]:
            res += common[j]
          else:
            break
        common = res
      
      return common


