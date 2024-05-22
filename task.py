def find_coins_greedy(amount, coins):
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins
    return result

def find_min_coins(amount, coins):
    # таблиця для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    # таблиця для відстеження використаних монет
    coin_count = [0] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_count[x] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_count[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result


if __name__ == "__main__":
    coins = [1, 2, 10, 50]
    change = int(input("Введіть суму решти (в копійках): "))
    # жадібний алгоритм
    print(f"Жадібний алгоритм: {find_coins_greedy(change, coins)}")  

    # динамічне програмування
    print(f"Динамічне програмування: {find_min_coins(change, coins)}")  