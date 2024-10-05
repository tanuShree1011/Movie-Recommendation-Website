import streamlit as st
import pickle
import pandas as pd
import math
st.title("Welcome to Kannada Movies")


mov_dict= pickle.load(open('mov_dict.pkl','rb'))
movie=pd.DataFrame(mov_dict)

id_list=list(movie['id'].values)
link_list=list(movie['link'].values)
genre_list=list(movie['genre'].values)
overview_list=list(movie['overview'].values)
rating_list=list(movie['rating'].values)
lang_list=list(movie['language'].values)
title_list=list(movie['title'].values)
kan=[]


for i in id_list:
    indi=id_list.index(i)
    if lang_list[indi] == "Kannada":
        kan.append(title_list[indi])
        
r= math.ceil(len(kan)/3)
k= -1
for l in range(r):
    col= st.columns(3)
    for cols in range(3):
        with col[cols]:
            k+=1
            if k>len(kan)-1:
                break
            if st.button(kan[k]):
                ind = title_list.index(kan[k])
                with st.container(border=True):
                    st.write('Movie ID: ',id_list[ind])
                    st.write('Genre: ', genre_list[ind])
                    st.write('Overview: ',overview_list[ind])
                    st.write('Rating: ',rating_list[ind])
                    st.write('Click on the link below to watch the movie ')
                    st.link_button("Watch Now",link_list[ind])