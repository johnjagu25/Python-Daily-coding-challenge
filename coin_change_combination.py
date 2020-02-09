def count(coins, m, n): 
	combinations = [0 for k in range(n+1)] 
	combinations[0] = 1
	for i in range(0,m): 
		for j in range(coins[i],n+1): 
			combinations[j] += combinations[j-coins[i]] 
	return combinations[n] 
coins = [3,2,5]
m = len(coins) 
amount = 12
x = count(coins, m, amount) 
print (x) 