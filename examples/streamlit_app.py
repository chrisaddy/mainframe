from typing import Tuple
import pandas as pd
import pyro.distributions as dist
import streamlit as st
from mainframe import Simulator
from mainframe.components import stochastic, deterministic
from dataclasses import dataclass


st.title("Simulate Data for a Two-Sample T-Test")


control_mean = st.sidebar.slider("control mean", min_value = 0, max_value=100, step=1)
control_variance = st.sidebar.slider("control variance", min_value = 1, max_value=20, step=1)
treatment_mean = st.sidebar.slider("treatment mean", min_value = 0, max_value = 100, step=1)
treatment_variance = st.sidebar.slider("treatment variance", min_value = 1, max_value = 100, step=1)
num_samples = st.sidebar.slider("treatment variance", min_value = 10, max_value = 10000, step=10)


@dataclass
class TwoSample(Simulator):
    control: Tuple[float, float] = (0, 1)
    treatment: Tuple[float, float] = (0, 1)

    def model(self):
        control = stochastic("control", dist.Normal(*self.control))
        treatment = stochastic("treatment", dist.Normal(*self.treatment))

    def dataframe(self):
        return pd.DataFrame(self.samples)

    def show(self):
        data = self.dataframe.melted(value_vars=["control", "treatment"])
        return px.violin(y="value", color="variable", data=data)


two_sample = TwoSample(control=(control_mean, control_variance), treatment=(treatment_mean, treatment_variance), num_samples=num_samples)
st.plotly_chart(two_sample.show())
