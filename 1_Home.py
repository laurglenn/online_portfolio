import streamlit as st
from PIL import Image

#Page Setup
about_page = st.Page(
    page="sections/about_me.py",
    title="About Me",
    icon=":material/account_circles:",
    default=True,
)
project_1_page = st.Page(
    page="sections/streamlitdash.py",
    title="Streamlit(Python) Sales Dashboard",
    icon=":material/dataset:",
    default=True,
)
project_2_page = st.Page(
    page="sections/tableaudash.py",
    title="About Me",
    icon=":material/account_circles:",
    default=True,
)
project_3_page = st.Page(
    page="sections/powerbidash.py",
    title="About Me",
    icon=":material/home:",
    default=True,
)


#Create Navigation
pg = st.navigation(pages=[about_page,project_1_page,project_2_page,project_3_page])

#Run Navigation
pg.run()

#Add in other places to view my work
#Links = {
#    "My Tableau Public":" https://public.tableau.com/app/profile/lauren.glenn/vizzes",
 #   "My PowerBI Gallery": "https://github.com",
 #   "My LinkedIn": "https://linkedin.com",
#}

#Create columns for contact links
#st.write('\n')
#cols = st.columns(len(Links))
#for index, (platform, link) in enumerate(Links.items()):
 #   cols[index].write(f"[{platform}]({link})")

#Summary of portfolio
#st.write('\n')
#st.subheader("CHANGE")
#st.write(
  #  """
#Welcome to my online portfolio! I have eight years of experience in deriving actionable insights from data and transforming them into engaging visualizations. 
#Explore the projects section to see examples of my work with various tools and technologies.

#"""
#)
