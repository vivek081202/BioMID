#importing streamlit to make python web app UI
import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser
st.set_page_config(layout="wide",
    page_title="BioMID | Home",
    page_icon="Images/face-scan.png",
    initial_sidebar_state="expanded"
    )


with st.sidebar:
    selected = option_menu(
        menu_title= "BioMID",
        options=["Home","Signup","Login"],
        icons=["house","door-open","key"],
        default_index=0,
        orientation= "verical",
        menu_icon="cast"
    )
    if selected =="Home":
        st.title(f"About AImob")
        st.write(
            """
  *BioMID* is web based tool which facilitates integrated AI tools for face recognition & image processing.\n
  **BioMID** is a technology capable of matching a human face from a digital image or a video frame against a database of faces. Such a system is typically employed to authenticate users through ID verification services, and works by pinpointing and measuring facial features from a given image. 
    """
        )
    if selected =="Signup":
        st.write("\n\n")
        st.write("""
        # Hello 👋, Sign Up Here    """)
        with st.form("Registeration"):
            RName = st.text_input('Name',placeholder='Enter Name')
            RPhone = st.text_input('Mobile',placeholder='Enter Mobile')
            REmail = st.text_input('Email',placeholder='Enter Email')
            RPassword = st.text_input('Password',placeholder='Enter Password',type="password")
            st.write("\n\n")
            Signup = st.form_submit_button('Register Me')

            if Signup:
                if RName != "" and RPhone != "" and REmail != "" and RPassword != "":
                    st.success("**Registered successfully**", icon="✅")
                elif RName == "" or RPhone == "" or REmail == "" or RPassword == "":
                    st.warning("Please! fill all fields", icon="⚠")
                else:
                    st.warning("Please! fill all fields", icon="⚠")

    if selected =="Login":
        st.write("""
        # Login 🔐""")
        with st.form("Registeration"):
            REmail = st.text_input('Email',placeholder='Enter Email')
            RPassword = st.text_input('Password',placeholder='Enter Password',type="password")
            st.write("\n\n")
            Login = st.form_submit_button('Login')

st.image('Images/facerobo.png',width = 125)
st.write("""
# BioMID - A Face Recognition Analyser
    """)

st.image("Images/Face.jpg",caption='BioM - Face Recognition Analyser')
st.write("""
**BioMID** simply checks to see whether there is, in fact, a person in a certain photograph or video. It uses machine learning algorithms to scan digital images for human faces, typically by looking for the eyes first and then calculating the edges of each human face. This is how the system pinpoints exactly where human faces are and counts how many people are present in a photo or video.
""")

st.write("""
# How it Works?
""")
st.write("""
**Face recognition technology** is one use of face detection. Where face detection simply identifies the presence of a face in an image, face recognition either verifies or identifies an actual person.

Once a system establishes that there is, in fact, a face present, it uses a series of algorithms to examine that face. The algorithms rely on specific details, such as:
\n
🔯 **How far apart are the eyes?**\n
🔯 **How high is the bridge of the nose?**\n
These details are known as “facial landmarks,” and the more landmarks a face recognition system can read, the more accurate the system will be. Those landmarks are used to create a precise mathematical representation of the face.
At this point, face recognition runs the face –- or rather, the mathematical representation of it — against an existing database of faces to find a match and identify the person in the picture.
""")

url = 'https://www.eff.org/pages/face-recognition'
bloglink = 'https://www.trio.dev/blog/facial-recognition-applications'
if st.button('Know More'):
    webbrowser.open_new_tab(url)

st.write("""
# Applications
""")

Education, Asecurity, Hcare = st.columns(3,gap="medium")

with Education:
   st.header("Education")
   st.image("Images/Education.jpg")
   st.write("A growing number of schools already use cameras that utilize facial recognition software to identify students, staff, unauthorized individuals, and even behavior that could present a threat to safety. This is one of many new tech trends that are transforming education.")
   if st.button('More on Education'):
        webbrowser.open_new_tab(bloglink)

with Asecurity:
   st.header("Automobile Security")
   st.image("Images/Automobile.jpg")
   st.write("In another capacity, facial recognition technology is sometimes used by ride-sharing apps to confirm that a given passenger is who they say they are. Or alternatively, the same technology can guarantee that the passenger is approaching the right driver. ")
   if st.button('More on Automobile security'):
        webbrowser.open_new_tab(bloglink)

with Hcare:
   st.header("Health Care")
   st.image("Images/Health.jpg")
   st.write("Applications of facial recognition technology are used in hospitals, especially those working in assisted living. The software serves to keep track of everything that is going on within a hospital, ensuring patients are safe and the premise is secure. ")
   if st.button('More on Health Care'):
        webbrowser.open_new_tab(bloglink)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position:relative;
left: 0;
bottom: 0;
width: 100%;
background-color: #FF4B4B;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Copyright &copy; 2022 All Rights Reserved by BioM</p>
Designed & developed by Ankita Kumari
</div>
"""
st.markdown(footer,unsafe_allow_html=True)