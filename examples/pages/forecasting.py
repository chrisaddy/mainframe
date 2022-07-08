import streamlit as st
import pandas as pd
import pyro.distributions as dist
from mainframe import Simulator
from mainframe.components import stochastic, deterministic
import plotly.express as px
from dataclasses import dataclass


st.title("Univariate Time Series Data")

slope = st.sidebar.slider("slope of trend", min_value=-100.0, max_value=100.0, step=0.1)
noise = st.sidebar.slider("noise", min_value=1.0, max_value=100.0, step=0.1)
num_days = st.sidebar.slider("number of days", min_value = 10, max_value = 500, step=10)


st.write("In the simplest case, simulating a univariate time series is just adding a trend to a random walk")

st.markdown("""
```python
@dataclass
class LinearTrend(Simulator):
    num_dates = 365
    slope = 5

    def model(self):

        day = stochastic("_day", dist.Uniform(0, 1))
        day = deterministic("day", (day * self.num_dates).round())

        brownian = stochastic("brownian", dist.Normal(0, 2))
        trend = deterministic("trend", self.slope * day + brownian)
```
""")

@dataclass
class LinearTrend(Simulator):
    num_dates: int = 365
    slope: float = 0
    noise: float = 1

    def model(self):

        day = stochastic("_day", dist.Uniform(0, 1))
        day = deterministic("day", (day * self.num_dates).round())

        brownian = stochastic("brownian", dist.Normal(0, self.noise))
        trend = deterministic("trend", self.slope * day + brownian)

    @property
    def dataframe(self):
        data = pd.DataFrame(self.samples)

        return data[["day", "trend"]].drop_duplicates(subset=["day"]).sort_values(by="day")

    def show(self):
        return px.line(x=self.dataframe.day, y=self.dataframe.trend)


linear_trend = LinearTrend(num_dates=num_days, slope=slope, noise=noise)

st.plotly_chart(linear_trend.show())

st.download_button("download simulated data", data=linear_trend.dataframe.to_csv().encode("utf-8"), mime="text/csv")
