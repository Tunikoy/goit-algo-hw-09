import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Тест продуктивності
amount = 10000

# Жадібний алгоритм
start_time = time.time()
find_coins_greedy(amount)
greedy_time = time.time() - start_time

# Динамічне програмування
start_time = time.time()
find_min_coins(amount)
dp_time = time.time() - start_time

print(f"Час виконання жадібного алгоритму: {greedy_time} секунд")
print(f"Час виконання алгоритму динамічного програмування: {dp_time} секунд")
