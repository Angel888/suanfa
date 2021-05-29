class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list):
        uglies = [0] * n
        primes_to_uglies_loc = [0] * len(primes)
        print("111", primes_to_uglies_loc)
        uglies[0] = 1
        for i in range(1, n):  # n=12
            # uglies[i]=primes[0]*primes_to_uglies_loc[0]
            # for x, y in zip(primes, primes_to_uglies_loc):
            #     if uglies[i]>x*uglies[y]:
            #         uglies[i]=x*uglies[y]
            print(list(zip(primes, primes_to_uglies_loc)))
            print("uglies",uglies)
            print("-----\n")
            uglies[i] = min(x * uglies[y] for x, y in
                            zip(primes, primes_to_uglies_loc))  # primes=[2,7,13,19] #primes_to_uglies_loc=[0, 0, 0, 0]
            for j in range(len(primes)):
                # print("primes[j] * uglies[primes_to_uglies_loc[j]]--",primes[j] * uglies[primes_to_uglies_loc[j]])
                if uglies[i] >= primes[j] * uglies[primes_to_uglies_loc[j]]:
                    primes_to_uglies_loc[j] += 1
                    # print(primes_to_uglies_loc)
        print(uglies)
        return uglies[-1]

    def nthSuperUglyNumber1(self, n: int, primes: list[int]) -> int:
        import heapq
        heap = [1]
        n -= 1
        while n:
            tmp = heapq.heappop(heap)
            while heap and tmp == heap[0]:
                tmp = heapq.heappop(heap)
            for p in primes:
                t = p * tmp
                heapq.heappush(heap, t)
            n -= 1
        return heapq.heappop(heap)

    def nthSuperUglyNumber2(self, n: int, primes: list[int]) -> int:
            import heapq
            uglies = [0] * n
            uglies[0] = 1
            visited = set()
            visited.add(1)
            primes_to_uglies_loc = [0] * len(primes)
            heap = []
            for idx, prime in enumerate(primes):
                heapq.heappush(heap, [prime, idx])
                visited.add(prime)

            for i in range(1, n):
                uglies[i], k = heapq.heappop(heap)

                while primes[k] * uglies[primes_to_uglies_loc[k]] in visited:
                    primes_to_uglies_loc[k] += 1
                heapq.heappush(heap, [primes[k] * uglies[primes_to_uglies_loc[k]], k])
                visited.add(primes[k] * uglies[primes_to_uglies_loc[k]])
            return uglies[-1]





if __name__ == '__main__':
    Solution().nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19])
