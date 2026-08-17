class Solution:
    def romanToInt(self, s: str) -> int:
      rom_to_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
      }

      count = 0
      s_size = len(s)

      for i in range(s_size):
        if i+1 < s_size and rom_to_num[s[i]] < rom_to_num[s[i+1]]:
          count -= rom_to_num[s[i]]
        else:
          count += rom_to_num[s[i]]
      return count