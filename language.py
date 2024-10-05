import streamlit as st
def app():
    st.write("At MovieMap, we celebrate the richness of cinema across languages and cultures. Our extensive collection features films from around the world, offering you the opportunity to explore diverse storytelling and unique perspectives. Whether you're drawn to the charm of Bollywood, the passion of Kannada films, or the innovation of Malayalam storytelling, there's a cinematic experience waiting for you in every language!")
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)
    with col1:
        st.image('hindi.png')
    with col2:
       st.image("kannada.png")
    with col3:
       st.image('telugu.png')
    with col4:
       st.page_link('pages/hindi.py', label='Explore Hindi Movies')
    with col5:
       st.page_link('pages/kannada.py', label='Explore Kannada Movies')
    with col6:
       st.page_link('pages/telugu.py', label='Explore Telugu Movies')
    with col7:
        st.image('english.png')
    with col8:
       st.image("malayalam.png")
    with col9:
       st.image('tamil.png')
    with col10:
       st.page_link('pages/english.py', label='Explore English Movies')
    with col11:
       st.page_link('pages/malayalam.py', label='Explore Malayalam Movies')
    with col12:
       st.page_link('pages/tamil.py', label='Explore Tamil Movies')