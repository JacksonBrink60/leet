"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""."""

strs = ["flower", "flow", "flight"]

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""
        first_word = strs[0]
        for idx in range(len(first_word)): # helps pick the character 
            for word_idx in range(1, len(strs)): # helps pick the word
                if len(strs[word_idx]) <= idx:
                    return common_prefix
                if strs[word_idx][idx] != first_word[idx]: # characters don't match return the common prefix
                    return common_prefix
            common_prefix += first_word[idx]
        return common_prefix



def main():
    sol = Solution()
    print(sol.longestCommonPrefix(strs=strs))


if __name__ == "__main__":
    main()
