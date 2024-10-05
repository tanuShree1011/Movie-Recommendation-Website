import streamlit as st
import pandas as pd
import pickle


def app():
    st.title('MOVIE MAP')
    st.write(
        'Welcome to MovieMap, your ultimate destination for movie recommendations! At MovieMap, we believe that every great film has the power to transport you to another world, spark meaningful conversations, and create lasting memories. Our mission is to help you discover films that resonate with your unique taste, whether you’re in the mood for an exhilarating action flick, a heartwarming drama, or a thought-provoking documentary.')
    
    def recommend(m):
        ind = movie[movie['title'] == m].index[0]
        distances = sorted(list(enumerate(similarity[ind])), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movie_names = []
        for i in distances:
            recommended_movie_names.append(movie.iloc[i[0]].title)
        return recommended_movie_names

    mov_dict= pickle.load(open('mov_dict.pkl','rb'))
    movie=pd.DataFrame(mov_dict)
    similarity= pickle.load(open('similarity_dict.pkl','rb'))
    title_list=list(movie['title'].values)
    link_list = list(movie['link'].values)
    option= st.selectbox('Select your movie',title_list)
    if st.button('Recommend'):
        rec= recommend(option)
        cols = st.columns(5)
        col=0
        for i in rec:
            ind= title_list.index(i)
            with cols[col]:
                col+=1
                if col > len(rec) :
                    break
                with st.container(border=True):
                    st.write(i)
                    st.link_button("Watch Now", link_list[ind])
          


    st.image('banner.png')