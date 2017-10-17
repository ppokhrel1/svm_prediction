from pssm_helpers import *
from calculate_pssm import *
#import `Sequential` from `keras.models`
from keras.models import Sequential
from sklearn.preprocessing import StandardScaler


# Import `Dense` from `keras.layers`
from keras.layers import Dense

# Initialize the constructor
model = Sequential()

# Add an input layer 
model.add(Dense(100, activation='relu', input_shape=(100,)))

# Add one hidden layer 
#model.add(Dense(100, activation='relu'))
model.add(Dense(20, activation='relu'))

# Add an output layer 
model.add(Dense(1, activation='sigmoid'))

X, y = training_sample()
model.compile(loss='mse',
    optimizer='adam',
    metrics=['accuracy'])

X_train = X[:round(0.75 * len(X)) ]
y_train = y[:round(0.75 * len(y)) ]

X_test = X[round(0.75 * len(X)) :]
y_test = y[round(0.75 * len(y)) :]

scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

epochs = 50
model.fit(X_train, y_train,epochs=epochs, batch_size=10, verbose=1)
#model.fit(X, y, validation_split=0.33, epochs=epochs, batch_size=20, verbose=2)
y_pred = model.predict(X_test)
score = model.evaluate(X_test, y_test,verbose=1)
#print(score)

print("\n%s: %.2f%%" % (model.metrics_names[1], score[1]*100))
