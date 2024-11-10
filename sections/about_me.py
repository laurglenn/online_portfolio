import streamlit as st

st.title("About Me")


#----CREATE SECTIONS FOR ABOUT ME PAGE-----
col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/img.jpg, width=230)
with col2:
    st.title("Lauren Glenn", anchor=False)
    st.write("Sales Analytics Analyst, .........)


#Add in other places to view my work
Links = {
    "My Tableau Public":" https://public.tableau.com/app/profile/lauren.glenn/vizzes",
    "My PowerBI Gallery": "https://github.com",
    "My LinkedIn": "https://linkedin.com",
}

#Create columns for contact links
st.write('\n')
cols = st.columns(len(Links))
for index, (platform, link) in enumerate(Links.items()):
    cols[index].write(f"[{platform}]({link})")
             


