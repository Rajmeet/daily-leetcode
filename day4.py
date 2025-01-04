# 1930. Unique Length-3 Palindromic Subsequences

# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

#     For example, "ace" is a subsequence of "abcde".

 

# Example 1:

# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")

# Example 2:

# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".

# Example 3:

# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # @staticmethod
        # def is_palindrome(s):
        #     return s == s[::-1]

        # @staticmethod
        # def calculate_all_subsequences(s):
        #     n = len(s)
        #     subsequences = set()
        #     for i in range(n):
        #         for j in range(i + 1, n):
        #             for k in range(j + 1, n):
        #                 subsequences.add(s[i] + s[j] + s[k])
        #     return subsequences
        
        # subsequences = calculate_all_subsequences(s)
        # unique_palindromes = {sub for sub in subsequences if is_palindrome(sub)}
        
        # return len(unique_palindromes)

        first_seen = {}
        last_seen = {}

        for i, char in enumerate(s):
            if char not in first_seen:
                first_seen[char] = i
            last_seen[char] = i
        
        unique = set()
        for char in set(s):
            left = first_seen[char]
            right = last_seen[char]

            if left < right:
                middle = set(s[left + 1:right])
                for m in middle:
                    unique.add((char, m, char))
        
        return len(unique)


s = Solution()
print(s.countPalindromicSubsequence("bbcbaba"))  # 4
print(s.countPalindromicSubsequence("aabca"))  # 3
print(s.countPalindromicSubsequence("adc"))  # 0