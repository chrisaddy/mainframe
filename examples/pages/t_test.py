from typing import Tuple
import pandas as pd
import pyro.distributions as dist
import streamlit as st
from mainframe import Simulator
from mainframe.components import stochastic, deterministic
from dataclasses import dataclass
import plotly.express as px


st.title("Simulate Data for a Two-Sample T-Test")


control_mean = st.sidebar.slider("control mean", min_value = 0, max_value=100, step=1)
control_variance = st.sidebar.slider("control variance", min_value = 1, max_value=20, step=1)
treatment_mean = st.sidebar.slider("treatment mean", min_value = 0, max_value = 100, step=1)
treatment_variance = st.sidebar.slider("treatment variance", min_value = 1, max_value = 100, step=1)
num_samples = st.sidebar.slider("number of samples to generate", min_value = 10, max_value = 10000, step=10)

st.write("In `mainframe`, models are added to `Simulator` classes. These models are, at their core, pyro models.In essence, we define a prior probability distribution over which the simulator samples.")

st.write("In the case of a simple two-sample T-Test")

st.markdown("""
```python
@dataclass
class TwoSample(Simulator):
    control: Tuple[float, float] = (0, 1)
    treatment: Tuple[float, float] = (0, 1)

    def model(self):
        control = stochastic("control", dist.Normal(*self.control))
        treatment = stochastic("treatment", dist.Normal(*self.treatment))
```
""")


@dataclass
class TwoSample(Simulator):
    control: Tuple[float, float] = (0, 1)
    treatment: Tuple[float, float] = (0, 1)

    def model(self):
        control = stochastic("control", dist.Normal(*self.control))
        treatment = stochastic("treatment", dist.Normal(*self.treatment))

    @property
    def dataframe(self):
        return pd.DataFrame(self.samples)

    def show(self):
        data = self.dataframe.melt(value_vars=["control", "treatment"])
        return px.violin(y=data.value, color=data.variable)


two_sample = TwoSample(control=(control_mean, control_variance), treatment=(treatment_mean, treatment_variance), num_samples=num_samples)
st.plotly_chart(two_sample.show())


st.download_button("download simulated data", data=two_sample.dataframe.to_csv().encode("utf-8"), mime="text/csv")
