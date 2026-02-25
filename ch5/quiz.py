# q18
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# q19
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)

# q20
from sklearn.linear_model import LinearRegression

model = LinearRegression()
y_pred = model.predict(X_test)
model.fit(X_train, y_train)