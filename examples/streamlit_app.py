import streamlit as st
from mainframe import Simulator
from mainframe.components import stochastic, deterministic


st.title("Mainframe")


st.slider("control mean", min_value = 0, max_value=100, step=1)
st.slider("treatment mean", min_value = 0, max_value = 100, step=1)



