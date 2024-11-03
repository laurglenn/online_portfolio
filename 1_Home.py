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
    "LinkedIn": "https://linkedin.com",
    "PowerBI Gallery": "https://github.com",
}

st.write('\n')
cols = st.columns(len(Links))
for index, (platform, link) in enumerate(Links.items()):
    cols[index].write(f"[{platform}]({link})")
