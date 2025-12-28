
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index= new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    for i in movie_list:
        print(new_df.iloc[i[0]].title)
        
        

movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)



st.title("Movie Recommendation System")

Select_movie_name=st.selectbox(
    'Select an option:',
    movies['title'].values
) 

if st.button('Recommend'):
    recommend(Select_movie_name)
    st.write("Recommended movies:", selected_movie_recommens)
    