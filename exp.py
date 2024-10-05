import streamlit as st

rate = st.slider("How much do you want to rate ?", 0, 10, 3)
st.write("Rating: ", rate)