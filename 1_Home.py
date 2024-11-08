import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Lauren's Portfolio"
)

st.title("Overview")
st.sidebar.success("Select a page above.")

#Add in other places to view my work
Links = {
    "Tableau Public":" https://public.tableau.com/app/profile/lauren.glenn/vizzes",
    "PowerBI Gallery": "https://github.com",
    "LinkedIn": "https://linkedin.com",
}

st.write('\n')
cols = st.columns(len(Links))
for index, (platform, link) in enumerate(Links.items()):
    cols[index].write(f"[{platform}]({link})")

#Summary
st.write('\n')
st.subheader("CHANGE")
st.write(
    """
Welcome to my online portfolio! I have eight years of experience in deriving actionable insights from data and transforming them into engaging visualizations. 
Explore the projects section to see examples of my work with various tools and technologies.

"""
)
