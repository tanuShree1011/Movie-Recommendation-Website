import streamlit as st
def app():
    st.write('At MovieMap, we offer a diverse array of movie genres to suit every taste and mood. Whether you’re seeking heart-pounding action, laugh-out-loud comedies, or thought-provoking dramas, our carefully curated selections cater to all film lovers. Explore each genre to discover hidden gems and beloved classics that promise to enhance your movie-watching experience!')
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)
    col13, col14, col15 = st.columns(3)
    col16, col17, col18 = st.columns(3)
    with col1:
        st.image('thriller.png')
    with col2:
       st.image("adventure.png")
    with col3:
       st.image('comedy.png')
    with col4:
       st.page_link('pages/thriller.py', label='Explore Thriller Movies')
    with col5:
       st.page_link('pages/adventure.py', label='Explore Adventure Movies')
    with col6:
       st.page_link('pages/comedy.py', label='Explore Comedy Movies')
    with col7:
        st.image('drama.png')
    with col8:
       st.image("romance.png")
    with col9:
       st.image('action.png')
    with col10:
       st.page_link('pages/drama.py', label='Explore Drama Movies')
    with col11:
       st.page_link('pages/romance.py', label='Explore Romance Movies')
    with col12:
       st.page_link('pages/action.py', label='Explore Action Movies')
    with col13:
        st.image('scifi.png')
    with col14:
       st.image("family.png")
    with col15:
       st.image('musical.png')
    with col16:
       st.page_link('pages/scifi.py', label='Explore Sci-Fi Movies')
    with col17:
       st.page_link('pages/family.py', label='Explore Family Movies')
    with col18:
       st.page_link('pages/musical.py', label='Explore Musical Movies')