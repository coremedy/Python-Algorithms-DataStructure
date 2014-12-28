'''
Created on 2014-12-23
Code coming from: http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
'''

def coin_change_dp(coin_list, change, minCoins, coinUsed):
    for cents in range(1, change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coin_list if c <= cents]:
            if minCoins[cents - j] + 1 <= coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

if __name__ == '__main__':
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for", amnt, "requires")
    print(coin_change_dp(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)