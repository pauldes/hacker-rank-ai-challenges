def transaction(m, k, d, name, owned, prices, strategy=1):
    rest = m
    if strategy==0:
        action = None
    elif strategy==1:
        buy_possible = prices[4]<m
        sell_possible = owned>=1
        delta_5 = prices[4] - prices[0]
        delta_4 = prices[4] - prices[1]
        delta_3 = prices[4] - prices[2]
        delta_2 = prices[4] - prices[3]
        #Sell if stock is over all previous days
        if sell_possible and delta_2>0 and delta_3>0 and delta_4>0 and delta_5>0:   
            action = f"{name} SELL 1"
        #Buy if stock is under all previous days
        elif buy_possible and delta_2<0 and delta_3<0 and delta_4<0 and delta_5<0:   
            action = f"{name} BUY 1"
            rest = rest - prices[4]
        else:
            action = None
    elif strategy==2:
        buy_possible = prices[4]<m
        sell_possible = owned>=1
        delta_5 = prices[4] - prices[0]
        delta_4 = prices[4] - prices[1]
        delta_3 = prices[4] - prices[2]
        delta_2 = prices[4] - prices[3]
        #Buy if stock is over all previous days except last
        if buy_possible and delta_2<0 and delta_3>0 and delta_4>0 and delta_5>0:   
            action = f"{name} BUY 1"
            rest = rest - prices[4]
        #Sell if stock is under all previous days except last
        elif sell_possible and delta_2>0 and delta_3<0 and delta_4<0 and delta_5<0:   
            action = f"{name} SELL 1"
        else:
            action = None
    elif strategy==3:
        buy_possible = prices[4]<m
        sell_possible = owned>=1
        delta_5 = prices[4] - prices[3]
        delta_4 = prices[3] - prices[2]
        delta_3 = prices[2] - prices[1]
        delta_2 = prices[1] - prices[0]
        #Sell if stock has been going up for 5 days
        if sell_possible and delta_2>0 and delta_3>0 and delta_4>0 and delta_5>0:   
            action = f"{name} SELL 1"
        #Buy if stock is going up since 2 days
        elif buy_possible and delta_2>0 and delta_3<0 and delta_4<0 and delta_5<0:   
            action = f"{name} BUY 1"
            rest = rest - prices[4]
        else:
            action = None
    return action, rest

inputs = input().split()
m = float(inputs[0])
k = int(inputs[1])
d = int(inputs[2])


actions = []

for i in range(k):
    if i==0:
        rest=m
    inputs = input().split()
    name = str(inputs[0])
    owned = int(inputs[1])
    prices = [float(s) for s in inputs[2:]]
    action, rest = transaction(rest, k, d, name, owned, prices)
    if action is not None:
        actions.append(action)
    
print(len(actions))
for action in actions:
    print(action)