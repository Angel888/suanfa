class Solution:
    def reverseWords(self, s: str) -> str:
        s_l=s.strip().split(" ")
        return "".join(s_l[::-1])
if __name__ == '__main__':
    s=Solution()
