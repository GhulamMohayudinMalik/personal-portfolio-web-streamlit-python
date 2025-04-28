import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)


with col1:
    st.image('images/my_image.png', width=600)


with col2:
    st.title("Ghulam Mohayudin")
    content = """
    Hi, I am Ghulam Mohayudin! I am a programmer, cyber security student, and technology enthusiast. I am in BS Cyber Security and Digital Forensics 7th semester in Islamia University of Bahawalpur. I am currently enhancing my Python and Web Development skills, and will be working in a little time, INSHA'ALLAH. 
    """
    st.info(content)

apps_detail = """Below you can find some of the apps I have built in Python. Feel free to contact me."""
st.write(apps_detail)