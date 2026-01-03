import streamlit as st
from datetime import time

st.slider('age', 0, 130, 25, 1)

st.slider("schedule your appointment",value=(time(11,30),time(12,45)))