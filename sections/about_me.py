import streamlit as st

#----CREATE SECTIONS FOR ABOUT ME PAGE-----
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/LaurenGlenn_Headshot.jpg", width=230)
with col2:
    st.title("Lauren Glenn", anchor=False)
    st.write("I’m a sales analytics analyst who enjoys bringing data to life through visualizations. I'm familiar with Tableau, PowerBI, Excel and Steamlit. Select one of the dashboards on the si")

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

#-----EXPERIENCES------#
st.write("\n")
st.subheader("Work Experience", anchor=False)
st.write(
    """
    -Sales Analytics Analyst, Pacific Life (October 2013-Present)\n
    -Reports Specialist, MetLife (January 2011-May 2013) \n
    """
    )

st.write("\n")
st.subheader("Skills & Certifications", anchor=False)
st.write(
    """
    -Alteryx Designer Certification \n
    -MicroStrategy 10 Certification \n
    -Snowflake(Create tables, views and queries using SQL) \n
    -Python(Basic pandas, openpyxl - This web app was created using Python) \n
    -Microsoft Excel(Pivot Tables, SUMIFS, CASE, WINDOWSUM)
    """
    )

     
             




