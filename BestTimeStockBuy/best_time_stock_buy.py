from collections import defaultdict


def maxProfit(prices: list[int]) -> int:
    value_index_mapping = defaultdict(int)

    for i, val in enumerate(prices):
        if val not in value_index_mapping:
            value_index_mapping[val] = i

    prices.sort()

    end = len(prices) - 1

    for i in range(end, 0, -1):
        smallest_val_index = value_index_mapping[prices[0]]
        largest_val_index = value_index_mapping[prices[i]]

        if smallest_val_index < largest_val_index:
            return prices[i] - prices[0]
    return 0

    # print(prices[i])


if __name__ == '__main__':

    # prices = [10, 1, 5, 6, 7, 1]
    prices = [3, 4, 1]
    print('max profit:', maxProfit(prices))

# Output: 6
