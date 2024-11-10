import streamlit as st
from PIL import Image

#Page Setup -- Emoji Google Material Symbols & Icons
about_page = st.Page(
    page="sections/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="sections/streamlitdash.py",
    title="Streamlit(Python) Sales Dashboard",
    icon=":material/grouped_bar_chart:",
)
project_2_page = st.Page(
    page="sections/tableaudash.py",
    title="Tableau Sales Dashboard",
    icon=":material/grouped_bar_chart:",
)
project_3_page = st.Page(
    page="sections/powerbidash.py",
    title="Power BI Sales Dashboard",
    icon=":material/grouped_bar_chart:",
)


#Create Navigation
#pg = st.navigation(pages=[about_page,project_1_page,project_2_page,project_3_page])

#Navigation with Sections
pg = st.navigation(
{
    "Info":[about_page],
    "Projects": [project_1_page,project_2_page,project_3_page]
}
    
)

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
