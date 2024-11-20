import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.title("Streamlit Sales Dashboard", anchor=False)
st.write('\n')
st.write("The dashboard below was created in Streamlit using the Python libaries streamlit, pandas and plotly. The data was created using Chat GPT. Under the dashboard some of the steps are listed")

#CSS STYLING
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

[data-testid="stMetricDeltaIcon-Up"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

[data-testid="stMetricDeltaIcon-Down"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

</style>
""", unsafe_allow_html=True)

#STREAMLIT LAYOUT
top_left_column, top_right_column = st.columns((2, 1))

with top_left_column:
    column_1, column_2, column_3, column_4 = st.columns(4)

   

#CONFIGS - Preselect data that will show up in filters

#PULL DATA




