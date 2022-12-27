import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide",
    page_title="BioMID | Documentation",
    page_icon="Images/face-scan.png")

with st.sidebar:
    selected = option_menu(
        menu_title= "BioMID (Documentation)",
        options=["Home"],
        icons=["house"],
        default_index=0,
        orientation= "vertical",
        menu_icon="cast",
    )
    if selected =="Home":
        st.title(f"About AImob")
        st.write(
            """
  *BioMID* is web based tool which facilitates integrated AI tools for face recognition & image processing.\n
  **BioMID** is a technology capable of matching a human face from a digital image or a video frame against a database of faces. Such a system is typically employed to authenticate users through ID verification services, and works by pinpointing and measuring facial features from a given image. 
    """
        )
st.image('Images/facerobo.png',width = 125)
st.write("""
# BioM - A Face Recognition Analyser
    """)

st.write("""
# Documentation
    """)

st.subheader("1. Face Recognition & Detection")
st.write("Face Detection Tutorial")
st.video("Videos/FD.webm")

st.write("\n\n")

st.subheader("2. Image Enchancement & Processing")
st.write("Image Processing tutorial")
st.video("Videos/Image_P.webm")

st.write("\n\n")

st.subheader("3. Facial Emotion Recognition")
st.write("FER Detection tutorial")
st.video("Videos/Emotion.webm")
