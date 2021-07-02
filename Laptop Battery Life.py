
# https://www.csvplot.com/

import pandas
from sklearn.linear_model import LinearRegression

train = pandas.read_csv("trainingdata.txt", header=None)

x_train = train[[0]]
y_train = train[1]

model = LinearRegression()
model.fit(x_train, y_train)

print(model.coef_, model.intercept_)

print(f"""
for i in range(100):
    x_test = float(input())
    #y_test = {model.coef_[0]}*x_test + {model.intercept_}
    y_test = min(x_test*2, 8.0)
    print(y_test)
""")
