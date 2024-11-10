import streamlit as st
import pandas as pd

st.title("Projects")
with st.sidebar:
  st.write("Streamlit(Python) Sales Dashboard")
  st.write("Tableau Sales Dashboard")
  st.write("Power BI Sales Dashboard")
  st.write("Excel Sales Dashboard")

st.sidebar.page_link("pages/portpages/3_Streamlit.py", label="Streamlit(Python) Sales Dashboard")

st.text("This is my _wireframe_ that I created through Figma. Creating a wireframe allows me to get a good idea of the look and feel of my dashboard. Figma allows you to also mim navagation to test user experience")


#if st.button("Streamlit(Python) Sales Dashboard"):
   # st.switch_page("portpages/3_Streamlit.py")
#if st.button("Tableau Sales Dashboard"):
    #st.switch_page("portpages/4_Tableau.py")
#if st.button("Power BI Sales Dashboard"):
   # st.switch_page("portpages/5_PowerBI.py")



#st.subheader("Units left", divider="red")

#need_to_reorder = df[df["units_left"] < df["reorder_point"]].loc[:, "item_name"]
#returns = df[df["returns"] > 100

#if len(returns) > 0:
    #items = "\n".join(f"* {name}" for name in need_to_reorder)

    #st.error(f"We're running dangerously low on the items below:\n {items}")
