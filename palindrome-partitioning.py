def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按键(key)排序:")

    print(dict(sorted(key_value.items(), key=lambda item: item[0])))


def main():
    # 调用函数
    dictionairy()


# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串 。返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。
#
#
# 示例 1：
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：
#
# 输入：s = "a"
# 输出：[["a"]]
# 链接：https://leetcode-cn.com/problems/palindrome-partitioning
# 主函数
class Solution:
    def partition(self, s: str):
        res = []
        for i in s:
            if i not in res:
                res.append(i)


class Solution1:
    def partition(self, s: str):
        result = []
        path = []

        # 判断是否是回文串
        def pending_s(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # 回溯函数，这里的index作为遍历到的索引位置，也作为终止判断的条件
        def back_track(s, index):
            # 如果对整个字符串遍历完成，并且走到了这一步，则直接加入result
            if index == len(s):
                result.append(path[:])
                return
            # 遍历每个子串
            # back_track是在遍历[index:i+1]的字符串，index<i<len(s)
            # 如果[index:i+1]是回文串，则继续遍历[i+1,j ]??? i <j<len(s)
            for i in range(index, len(s)):  # todo index有什么用？ 从index遍历到最右边
                # 剪枝，因为要求每个元素都是回文串，那么我们只对回文串进行递归，不是回文串的部分直接不care它
                # 当前子串是回文串
                if pending_s(s[index: i + 1]):
                    # 加入当前子串到path
                    path.append(s[index: i + 1])
                    # 从当前i+1处重复递归
                    back_track(s, i + 1) # todo s[index: i + 1]
                    # 回溯
                    path.pop()

        back_track(s, 0)
        return result

# todo 只有一个串是回文串时，它的子串才有可能是回文串？？？
if __name__ == "__main__":
    s_1=Solution1()
    s_1.partition("aab")
