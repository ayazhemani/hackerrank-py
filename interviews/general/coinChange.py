import unittest

class Solution:
    def coinChange(self, coins: list(), amount: int) -> int:
        coins = sorted(coins)[::-1]
        count = {}
        for coin in coins:
            count[coin] = amount//coin
            amount -= coin*count[coin]

        if amount == 0:
            return(sum(count[x] for x in count))
        else:
            return -1

class TestSolution(unittest.TestCase):
    def test_coinChange1(self):
        sol = Solution()
        coins = [1,2,5]
        amount = 11
        self.assertEqual(sol.coinChange(coins, amount), 3)

    def test_coinChange2(self):
        sol = Solution()
        coins = [2]
        amount = 3
        self.assertEqual(sol.coinChange(coins, amount), -1)

    def test_coinChange3(self):
        sol = Solution()
        coins = [1]
        amount = 0
        self.assertEqual(sol.coinChange(coins, amount), 0)

    def test_coinChange4(self):
        sol = Solution()
        coins = [1]
        amount = 1
        self.assertEqual(sol.coinChange(coins, amount), 1)

    def test_coinChange5(self):
        sol = Solution()
        coins = [1]
        amount = 2
        self.assertEqual(sol.coinChange(coins, amount), 2)

unittest.main(exit=False)
