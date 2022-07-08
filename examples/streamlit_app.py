import streamlit as st
from mainframe import Simulator
from mainframe.components import stochastic, deterministic


st.title("Simulate Data for a Two-Sample T-Test")


control_mean = st.sidebar.slider("control mean", min_value = 0, max_value=100, step=1)
control_variance = st.sidebar.slider("control variance", min_value = 0, max_value=20, step=1)
treatment_mean = st.sidebar.slider("treatment mean", min_value = 0, max_value = 100, step=1)
treatment_variance = st.sidebar.slider("treatment variance", min_value = 0, max_value = 100, step=1)


class TwoSample(Simulator):
    control: Tuple[float, float]
    treatment: Tuple[float, float]

    def model(self):
        control = stochastic("control", dist.Normal(*self.control))
        treatment = stochastic("control", dist.Normal(*self.treatment))


two_sample = TwoSample(control=(control_mean, control_variance), (treatment_mean, treatment_variance))
st.markdown(two_sample.samples.head())



