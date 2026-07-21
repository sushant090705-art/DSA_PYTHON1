# #bruteforce
# prices=[1,2,3,4,5,65,6,]
# n=len(prices)
# max_profit=0
# for i in range (0,n):
#     for j in range (i+1,n):
#         if prices[j]>prices[i]:
#             p=prices[j]-prices[i]
#             max_profit=max(max_profit,p)
# print(max_profit)            

#optimal solution
prices = [4, 65, 76, 7, 7, 6, 5]

n = len(prices)
maxprofit = 0
minprice = float("inf")

for i in range(n):
    minprice = min(minprice, prices[i])
    maxprofit = max(maxprofit, prices[i] - minprice)

print(maxprofit)