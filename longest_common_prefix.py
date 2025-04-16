"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string."""

strs = ["flower", "flow", "flight"]

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lis = ""
        for i in range(len(strs)):
            for h in strs[i]:
                lis = strs[0][i]
                if h == lis:
                    break


#go into the word
#go to first letter
#set said letter                 