# 1400. Construct K Palindrome Strings
# Solved
# Medium
# Topics
# Companies
# Hint

# Given a string s and an integer k, return true if you can use all the characters in s to construct k
# palindrome strings
# or false otherwise.

# Example 1:
# Input: s = "annabelle", k = 2
# Output: true
# Explanation: You can construct two palindromes using all characters in s.
# Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

# Example 2:

# Input: s = "leetcode", k = 3
# Output: false
# Explanation: It is impossible to construct 3 palindromes using all the characters of s.

# Example 3:

# Input: s = "true", k = 4
# Output: true
# Explanation: The only possible solution is to put each character in a separate string.


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Handle edge cases
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        # Initialize frequency dictionary and odd_count
        freq = [0] * 26
        odd_count = 0

        # Increment the value of the index corresponding to the current character
        for char in s:
            freq[ord(char) - ord("a")] += 1
        # Count the number of characters that appear an odd number of times in s
        for count in freq:
            if count % 2 == 1:
                odd_count += 1
        # Return if the number of odd frequencies is less than or equal to k
        return odd_count <= k