import streamlit as st

#----CREATE SECTIONS FOR ABOUT ME PAGE-----
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/LaurenGlenn_Headshot.jpg", width=230)
with col2:
    st.title("Lauren Glenn", anchor=False)
    st.write("I’m a sales analytics analyst who enjoys bringing data to life through visualizations.")

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
    -adfasdfa
    -asdfasd
    -aadfasf
    -asdfa
    -asdfsad
    """
    )

st.write("\n")
st.subheader("Skills & Certifications", anchor=False)
st.write(
    """
    -Alteryx Designer Certification
    -MicroStrategy 10 Certification
    -aadfasf
    -asdfa
    -asdfsad
    """
    )

     
             




