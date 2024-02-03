class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize dictionaries to store character frequencies
        freq_s = {}
        freq_t = {}

        # Count character frequencies in string s
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        # Count character frequencies in string t
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Compare frequencies to find the added letter
        for char in freq_t:
            if char not in freq_s or freq_t[char] > freq_s[char]:
                return char
