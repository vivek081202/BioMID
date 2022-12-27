import streamlit as st
from streamlit_option_menu import option_menu
import cv2
from fer import FER
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
 
st.set_page_config(layout="wide",
    page_title="BioMID | Emotion Detection",
    page_icon="Images/face-scan.png")

with st.sidebar:
    selected = option_menu(
        menu_title= "BioMID (FER)",
        options=["Home"],
        icons=["house"],
        default_index=0,
        orientation= "vertical",
        menu_icon="cast",
    )
    if selected =="Home":
        st.title(f"About FER Detection")
        st.write(
            """
  **BioMID's** uses technology that analyses facial expressions from both static images and videos in order to reveal information on one's emotional state. \n
    It uses process of identifying or verifying the identity of a person using their face. It captures, analyzes, and compares patterns based on the person's facial details. The face detection process is an essential step in detecting and locating human faces in images and videos.
    """
        )
#Emotions = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
# face_analysis = DeepFace.analyze(img_path = "Images/smile.jpg")
# st.write(face_analysis)

st.image('Images/face-scan.png',width = 125)
st.title("Facial Emotion Detection App")


# st.success("""
# # Sorry for inconvenience (Partially Developed)!
# FERD module is under development will be deployed soon.\n
# **Ankita Kumari, Developer [BioMID]**
# """)

input_image = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
if input_image is not None:
    st.success('Image Uploaded Successfully', icon="✅")
    st.subheader("Original Uploaded Image")
    st.image(input_image)

F_emotions = st.button("Analyse Emotions")

if F_emotions:
    input_image = cv2.imread("Images/smile.jpg")
    emotion_detector = FER(mtcnn=True)
    # Output image's information
    result = emotion_detector.detect_emotions(input_image)
    st.write(result)
