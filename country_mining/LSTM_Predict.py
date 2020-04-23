import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout,LSTM
from keras.models import Model
from keras.layers import Input, Dense
import pandas as pd

model = Sequential()
model.add(Dense(36, input_dim=3, activation='relu'))
model.add(Dense(18, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['mse'])