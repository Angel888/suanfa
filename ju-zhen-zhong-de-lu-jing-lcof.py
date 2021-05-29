class Solution:
    def exist(self, board, word: str):
        self.directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self.board = board
        self.word_list = list(word)
        self.w_l = len(self.word_list)
        self.h = len(self.board)
        self.l = len(self.board[0])
        self.walked = []
        for i in range(self.h):
            for j in range(self.l):
                self.walked = []
                self.k = 0

                # self.f = False
                # if i == 0 and j == 0:
                #     self.f = True

                if self.compare_char(i, j, 0, []):
                    return True
        return False

    def compare_char(self, i, j, k, walked):
        # if self.f and i == 2 and j == 0:
        #     print(self.k, self.word_list, self.board[i][j] == self.word_list[self.k] )
        if -1 < i < self.h and -1 < j < self.l and self.board[i][j] == self.word_list[k] and k < self.w_l - 1 and [i, j] not in walked :
            for d in self.directions:
                # if self.f and k == 2:
                #     print(self.board[i][j], [i,j], walked, d, k+1)
                # if self.compare_char(i + d[0], j + d[1], k+1, walked+[[i, j]]):
                walked.append([i, j])
                if self.compare_char(i + d[0], j + d[1], k+1, walked):
                     return True
            return False
        elif -1 < i < self.h and -1 < j < self.l and self.board[i][j] == self.word_list[k] and k == self.w_l - 1 and [i, j] not in walked :
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    a=s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
    # a=s.exist(board = [["a","b"],["c","d"]], word = "abcd")
    a = s.exist([["a", "a"]], "aaa")
    # a = s.exist([["C","A","A"],
    #              ["A","A","A"],
    #              ["B","C","D"]],"AAB")  # todo
    a = s.exist([["A","B","C","E"],
                 ["S","F","E","S"],
                 ["A","D","E","E"]],"ABCESEEEFS")
    print(a)
