import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import difflib

m_data = pd.DataFrame(pickle.load(open('movie.pkl','rb')))
similarity = pickle.load(open('similarity.pkl','rb'))
def movies(movie_name):
    list_of_all_titles=m_data['movie_title'].tolist()
    find_close_match=difflib.get_close_matches(movie_name,list_of_all_titles)
    l=m_data.loc[m_data['movie_title']==find_close_match[0]].index.values[0]
    
    similarity_score=list(enumerate(similarity[l]))
    sorted_sm=sorted(similarity_score,key=lambda x:x[1],reverse=True)
    r_movies=[]
    links=[]
    urls=[]
    for movie in sorted_sm:
        index=movie[0]
        title=m_data[m_data.index==index]['movie_title'].values[0]
        img_url=m_data[m_data.index==index]['img_url'].values[0]
        pagen=m_data[m_data.index==index]['linkfname'].values[0]
        if index<=10:
            r_movies.append(title)
            links.append(img_url)
            urls.append(pagen)
    return r_movies,links,urls

##def recommend(anime_name):
##    anime_index = anime_data[anime_data['title']== anime_name].index[0]
##    distance = similarity[anime_index]
##    anime_list = sorted(list(enumerate(distance)),reverse = True,key = lambda x:x[1])[1:11]
##    recommended_anime_name = []
##    recommended_anime_poster =[]
##    recommended_anime_link = []
##    for i in anime_list:
##        recommended_anime_name.append(anime_data.iloc[i[0]][0])
##        recommended_anime_poster.append(anime_data.iloc[i[0]][3])
##        recommended_anime_link.append(anime_data.iloc[i[0]][4])
##    return recommended_anime_name,recommended_anime_poster,recommended_anime_link
##
##st.title('Anime Recommendation')
##selected_anime_name = st.selectbox(
##    'Choose Anime Name',
##    (anime_data['title'].values))
##
##if st.button('Recommend'):
##    name,poster,link
##    = recommend(selected_anime_name)
##
##    for i in range(len(name)):
##        data = (f'{name[i]}')
##        caption = f"<h2>{data}</h2>"
##        st.markdown(caption , unsafe_allow_html=True)
##        st.markdown(f'<a href="{link[i]}" target="_blank">Click Here To Explore More</a>', unsafe_allow_html=True)
##        st.image(poster[i])


st.title('Movie Recommendation')
selected_movie_name = st.selectbox(
    'Choose Movie Name',
    (m_data['movie_title'].values))

if st.button('Recommend'):
    name,imgs,link=movies(selected_movie_name)

    for i in range(len(name)):
        data = (f'{name[i]}')
        caption = f"<h2>{data}</h2>"
	
        st.markdown(caption , unsafe_allow_html=True)
        st.markdown(f'<a href="{link[i]}" target="_blank">Click Here To Explore More</a>', unsafe_allow_html=True)
        if imgs[i]=='0':
            st.image('https://media.istockphoto.com/id/1216251206/vector/no-image-available-icon.jpg?s=312x312&w=0&k=20&c=6C0wzKp_NZgexxoECc8HD4jRpXATfcu__peSYecAwt0=')
        else:
            st.image(imgs[i])
       
  #reduce the image size only
