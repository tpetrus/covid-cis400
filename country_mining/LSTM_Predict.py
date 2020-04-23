import numpy as np
import keras
import sklearn
from sklearn import preprocessing
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout,LSTM
from keras.models import Model
from keras.layers import Input, Dense
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

pd.reset_option('display.max_columns')
pd.reset_option('display.max_rows')

le = preprocessing.LabelEncoder()
categories = ['AU','CN','ES','IT','US','VE']
le.fit(categories)

data = pd.read_csv('data\sorted_master.csv')
date = pd.to_datetime(data['date'],infer_datetime_format=True)


new_cases = data['new_daily_cases']
new_deaths = data['new_daily_deaths']
total_cases = data['total_cases']
total_deaths = data['total_deaths']
country = pd.DataFrame(data=le.transform(data['ID']))
type(country)


x = pd.concat([new_deaths,
            total_cases,total_deaths,country], 
            axis=1,sort=False)


y = new_cases

x_train = x.iloc[0:380]
type(x_train)

x_test = x.iloc[380:385]
y_train = new_cases[0:380]
y_test = new_cases[380:385]


#Create Model
keras.backend.clear_session()
model = Sequential()
model.add(Dense(32, input_dim=4, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['mse'])

#Set Layers
layer_0_weights = model.layers[0].get_weights()[0]
layer_0_biases = model.layers[0].get_weights()[1]

layer_1_weights = model.layers[1].get_weights()[0]
layer_1_biases = model.layers[1].get_weights()[1]

layer_2_weights = model.layers[2].get_weights()[0]
layer_2_biases = model.layers[2].get_weights()[1]

layer_3_weights = model.layers[3].get_weights()[0]
layer_3_biases = model.layers[3].get_weights()[1]



print(layer_0_weights.shape)
print(layer_0_biases.shape)

print(layer_1_weights.shape)
print(layer_1_biases.shape)

print(layer_2_weights.shape)
print(layer_2_biases.shape)

print(layer_3_weights.shape)
print(layer_3_biases.shape)

#Compiling,Fitting,and evaluating
model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['mse'])
model.fit(x_train, y_train, epochs=3000, batch_size=15)
print(model.predict(x_test))
print(model.evaluate(x_test,y_test))