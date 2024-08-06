"""https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/"""

def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


haystack = "butsad"
needle = "sad"
print(strStr(haystack, needle))