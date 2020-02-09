import sys 
def minCoins(coins, m, n): 
	combinations = [sys.maxsize for i in range(n + 1)] 
	combinations[0] = 0
	for i in range(m): 
		for j in range(coins[i], n + 1): 
			sub_res = combinations[j - coins[i]] 
			if (sub_res != sys.maxsize and sub_res + 1 < combinations[j]): 
				combinations[j] = sub_res + 1					
	return combinations[n] if combinations[n] != sys.maxsize else 0

if __name__ == "__main__": 

	coins = [1,2,5]
	m = len(coins) 
	n = 11
	print(minCoins(coins, m, n))


