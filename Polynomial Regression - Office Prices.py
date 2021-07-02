from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline

n_features, len_train = input().split()
x_train = []
y_train = []
for i in range(int(len_train)):
    line_input = input().split()
    x_train.append([float(n) for n in line_input[:-1]])
    y_train.append(float(line_input[-1:][0]))
    
    
degree = 3
scaler = StandardScaler()
model = make_pipeline(PolynomialFeatures(degree),scaler,LinearRegression())
model.fit(x_train, y_train)
    
len_test = input()
for i in range(int(len_test)):
    x_test = [float(n) for n in input().split()]
    res = model.predict([x_test])
    print(res[0])
