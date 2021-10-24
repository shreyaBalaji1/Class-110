import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import csv
import pandas as pd

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

#function to get mean of the given data samples
def randomSetOfMean(count):
    dataset = []
    for i in range(0,count):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

#function to plot the various mean on the graph
def show_fig (meanList) :
    df = meanList
    mean = st.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "Mean List"))
    fig.show()

def setup():
    meanList = []
    for i in range(0,1000) :
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)

    show_fig(meanList)
    mean = st.mean(meanList)
    stdev = st.stdev(meanList)
    print(mean)
    print(stdev)
    

setup()