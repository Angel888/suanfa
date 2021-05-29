class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
    # def letterCombinations(self, digits: str):
    #     """
    #     如果小于index，则先回溯所有可能的情况，再pop掉这一位；
    #     如果等于index，则加入结果中
    #     :param digits:
    #     :return:
    #     """
    #     if not digits:
    #         return list()
    #
    #     phoneMap = {
    #         "2": "abc",
    #         "3": "def",
    #         "4": "ghi",
    #         "5": "jkl",
    #         "6": "mno",
    #         "7": "pqrs",
    #         "8": "tuv",
    #         "9": "wxyz",
    #     }
    #     l=len(digits)
    #     def back_track(index,combination):  #todo 为什么答案不需要combination??
    #         print(combination)
    #         if index==l:
    #             combinations.append("".join(combination))
    #         else:
    #             for i in phoneMap[digits[index]]:
    #                 combination.append(i)
    #                 back_track(index+1,combination)
    #                 combination.pop()
    #     combinations=[]
    #     combination=[]
    #     back_track(0,combination)
    #     print(combinations)
    #     return combinations
if __name__ == '__main__':
    Solution().letterCombinations("234")
