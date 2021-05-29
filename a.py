from _ast import List

# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

class Solution2:
    def letterCombinations(self, digits: str) :
        if not digits:
            return []

        num2str = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        total = 1
        ss = []
        for i in digits:
            ss.append(num2str[i])
            # ss=[['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i']]
            total *= len(num2str[i])
            # total= 1*3*3*3=27
            print("total----",total)
        res = []
        for i in range(total):  # total=27
            tmp = []
            tmp_index = 1
            for s in ss:
                # ss=[['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i']]
                print("i-------",i)
                tmp.append(s[int(i / tmp_index) % len(s)])  # len(s)=3   tmp_index的值是3，9，27
                print("tmp_index------",tmp_index,"tmp--------",tmp,"int(i / tmp_index) % len(s)----",int(i / tmp_index) % len(s))
                tmp_index *= len(s)
            res.append(''.join(tmp))
        return res
    def letterCombinations3(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


class Solution3:
    def letterCombinations2(self, digits: str) :
        if not digits:
            return []

        num2str = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        ss = ['']
        #eg 23
        for i in digits:
            tmp = []
            for j in ss:
                for p in num2str[i]:
                    tmp.append(j + p)
            ss = tmp

            # if len(ss)==0:  # todo 我这个为啥超出内存限制了？
            #     # ss=[p for p in num2str[i]] #
            #     ss=num2str[i]
            # else:
            #     for j in ss:
            #         for p in num2str[i]:
            #             ss.append(j+p)
            #         ss.remove(j)
        return ss


class Solution4:
    # todo 时间复杂度为什么是3M次方？
    def letterCombinations5(self, digits: str):
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
        # 每个组合放到combinations后，
        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))  # 转为list
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    print(combination)
                    backtrack(index + 1)
                    combination.pop()
                    print("-------")
                    print(combination)


        combination = list()
        combinations = list()
        backtrack(0)
        return combinations




if __name__ == '__main__':
    print(Solution3().letterCombinations2('234'))