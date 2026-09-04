
def maxProfit(prices: list[int]) -> int:
    l = 0
    r = 1
    highest = 0

    while r < len(prices):

        if prices[l] < prices[r]:
            highest = max(highest, prices[r] - prices[l])
        else:
            l = r
        r += 1
    return highest


if __name__ == '__main__':
    # prices = [10, 1, 5, 6, 7, 1]
    # prices = [3, 4, 1]
    prices = [2, 1, 2, 1, 0, 1, 2]
    print('max profit:', maxProfit(prices))
