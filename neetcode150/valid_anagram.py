class Solution(object):
    def isAnagram(self, s, t):
        s_state = []
        for i in range(len(s)):
            found = False
            for j in range(len(t)):
                if s[i] == t[j]:
                    found = True
            s_state.append(found)
        
        return all(s_state)
      




        