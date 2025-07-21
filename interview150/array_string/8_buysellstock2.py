prices = [1,2,3,4,5]
profit=0
prices= [9999]+prices
for i in range(1,len(prices)):
    if prices[i]>prices[i-1]:
        profit+=prices[i]-prices[i-1]
print(profit)