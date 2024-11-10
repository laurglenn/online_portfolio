import streamlit as st

st.title("About Me")


#----CREATE SECTIONS FOR ABOUT ME PAGE-----
col1, col2, col3 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/LaurenGlenn_Headshot.jpg, width=230)
with col2:
    st.title("Lauren Glenn", anchor=False)
    st.write("Sales Analytics Analyst, .........")
with col3:
    st.title("Links Test")




