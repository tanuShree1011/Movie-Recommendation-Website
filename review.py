import pickle
import streamlit as st
import pandas as pd
import math


def app():
    st.title('Review Page')
    st.write('At Movie Map, we allow you to add your reviews on all kind of movies, you can also see what people have posted about the movie.')
    df = pd.read_csv("review.csv")
    review_list = list(df['Review'].values)
    mov_list = list(df['Movie'].values)
    mov_dict = pickle.load(open('mov_dict.pkl', 'rb'))
    movie = pd.DataFrame(mov_dict)
    title_list = list(movie['title'].values)
    tab1, tab2 = st.tabs(["View Reviews", 'Add Reviews'])
    with tab1:
        r = math.ceil(len(title_list) / 2)
        k = -1
        for l in range(r):
            col = st.columns(2)
            for cols in range(2):
                with col[cols]:
                    k += 1
                    if k > len(title_list) - 1:
                        break
                    if st.button(title_list[k]):
                        if title_list[k] in mov_list:
                            for i in range(len(mov_list)):
                                if mov_list[i] == title_list[k]:
                                    with st.container(border=True):
                                        st.write(review_list[i])
                        else:
                            st.write("No reviews yet")

    with tab2:
        with st.form("my_form"):
            st.write("Add your review")
            data = st.selectbox('Select your movie', title_list)
            statement = st.text_input('Write review down', '')
            if st.form_submit_button('Submit'):
                new = {"Movie": data, "Review": statement}
                df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
                df.to_csv("review.csv", index=False)