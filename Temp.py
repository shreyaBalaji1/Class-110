import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go
import csv
import random

df = pd.read_csv("data.csv")
data = df['temp'].tolist()

population_mean = st.mean(data)

stdev = st.stdev(data)

print(population_mean)
print(stdev)

""" fig = ff.create_distplot([data], ['temp'], show_hist = False)
fig.add_trace(go.Scatter(x = [population_mean, population_mean], y = [0,1], mode = "lines", name = "Mean"))
fig.show() """

#Code to find mean & stdev of randomly selected 100 data points
dataset = []
for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)

mean = st.mean(dataset)
stdev1 = st.stdev(dataset)

print(mean)
print(stdev1)