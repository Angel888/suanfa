class Solution:
    def lengthOfLongestSubstring(self, s):
        # i,j=0,0
        i = 0
        l = 0
        max_len = 0
        if not s:
            return 0
        char_set = set()
        for a in s:
            l += 1
            while a in char_set:
                char_set.remove(s[i])
                i += 1
                l -= 1
            char_set.add(a)
            if l>max_len:
                max_len=l
        return max_len

    def lengthOfLongestSubstring1(self, s):
        if not s: return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("tmmzuxt"))
