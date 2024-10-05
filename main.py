import streamlit as st
import pandas as pd
import home,  genre, language, kids, review, about
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(
    page_title="homepage", layout="wide"
)

st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', os.getenv('analytics_tag'));
        </script>
    """, unsafe_allow_html=True)
print(os.getenv('analytics_tag'))


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='🍿 🎬 MovieMap ',
                options=['Home', 'Genres', 'Languages', '🎈   Kids', 'Review', 'About Us'],
                icons=['house','person-fill','globe','   ','star-fill','info-circle'],
                menu_icon='  ',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "pink"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )

        if app == "Home":
            home.app()
        if app == "Languages":
            language.app()
        if app == 'Genres':
            genre.app()
        if app == '🎈   Kids':
            kids.app()
        if app == 'Review':
            review.app()
        if app == 'About Us':
            about.app()
    run()
