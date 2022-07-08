import streamlit as st
import pandas as pd
import pyro.distributions as dist
from mainframe import Simulator
from mainframe.components import stochastic, deterministic
import plotly.express as px


st.title("Univariate Time Series Data")

slope = st.sidebar.slider("slope of trend", min_value=-100.0, max_value=100.0, step=0.1)
num_samples = st.sidebar.slider("number of days", min_value = 10, max_value = 500, step=10)

class LinearTrend(Simulator):
    num_dates = 365
    slope = 5

    def model(self):

        day = stochastic("_day", dist.Uniform(0, 1))
        day = deterministic("day", (day * self.num_dates).round())

        brownian = stochastic("brownian", dist.Normal(0, 2))
        trend = deterministic("trend", self.slope * day + brownian)

    @property
    def dataframe(self):
        data = pd.DataFrame(self.samples)

        return data[["day", "trend"]].drop_duplicates(subset=["day"]).sort_values(by="day")

    def show(self):
        return px.line(x=data.day, y=self.data.trend)


linear_trend = LinearTrend(num_samples=10000)
st.dataframe(linear_trend.dataframe)
