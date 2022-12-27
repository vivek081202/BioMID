import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide",
    page_title="BioMID | Contact Us",
    page_icon="Images/face-scan.png")


with st.sidebar:
    selected = option_menu(
        menu_title= "BioM",
        options=["Home"],
        icons=["house"],
        default_index=0,
        orientation= "verical",
        menu_icon="cast",
    )
    if selected =="Home":
        st.title("About Developer")
        st.write("\n")
        st.write("""
        **👩 Developer:** Ankita Kumari\n
        **📧 Gmail:** globalankita24@gmail.com
        """)

st.image('Images/facerobo.png',width = 125)
st.write("""
# BioM - A Face Recognition Analyser
    """)

st.write("""
# Contact Us Info
    """)

image = """
<style> 

</style>

"""

Name = st.text_input('Name',placeholder='Enter Name')
Phone = st.text_input('Mobile',placeholder='Enter Mobile')
Email = st.text_input('Email',placeholder='Enter Email')
Message = st.text_area('Message',placeholder='Enter Your Message Here...')
submit = st.button("Submit")

if submit:
    if Name != "" and Phone != "" and Email != "" and Message != "":
        st.success("**Your message sent successfully**", icon="✅")
    elif Name == "" or Phone == "" or Email == "" or Message == "":
        st.warning("Please! fill all fields", icon="⚠")
    else:
        st.warning("Please! fill all fields", icon="⚠")
