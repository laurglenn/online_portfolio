import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.title("Streamlit Sales Dashboard", anchor=False)
st.write('\n')
st.write("The dashboard below was created in Streamlit using the Python libaries streamlit, pandas and plotly. The data was created using Chat GPT. Under the dashboard some of the steps are listed")

st.set_page_config(
    page_title="Makeuprama Sales Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
#CONFIGS - Preselect data that will show up in filters

#PULL DATA




