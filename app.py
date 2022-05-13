import streamlit as st
import pickle
import pandas as pd


def recommend(animes_):
    index = anime_[anime_['title'] == animes_].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_anime = []
    recommended_anime_poster = []
    for i in distances[0:31]:
        anime_id = anime_.iloc[i[0]].uid
        recommended_anime_poster.append(anime_.iloc[i[0]].img_url)
        recommended_anime.append(anime_.iloc[i[0]].title)
    return recommended_anime,recommended_anime_poster

def synopsis(animes_):
    index = anime_[anime_['title'] == animes_].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    i = distances[0]
    return temp.iloc[i[0]].synopsis, temp.iloc[i[0]].episodes, temp.iloc[i[0]].genre, temp.iloc[i[0]].aired

st.set_page_config(layout="wide")
st.header('Anime Recommender system')
animes = pickle.load(open('anime_dict.pkl','rb'))
anime_ = pd.DataFrame.from_dict(animes)
similarity = pickle.load(open('similarity.pkl','rb'))
temp = pd.DataFrame.from_dict(pickle.load(open('temp_dict.pkl','rb')))

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

anime_list = anime_['title'].values
selected_anime = st.selectbox(
    "Type or select an anime from the dropdown",
    anime_list
)
if st.button('Show Recommendations'):
    recommended_anime,recommended_anime_posters = recommend(selected_anime)
    genre , aired =[], []
    des, ep, genre, aired = synopsis(selected_anime)

    c1,c2,c3,c4 = st.columns(4)
    with c1:
        st.header(recommended_anime[0])
        st.image(recommended_anime_posters[0])

    with c2:
        st.subheader('Synopsis')
        st.write(des)

    with c3:
        st.subheader('Genres')
        st.write(genre)

    with c4:
        st.subheader('Episodes')
        st.write(ep)

        st.subheader('Aired Date')
        st.write(aired)

    col1, col2, col3, col4, col5 = st.columns(5)
    col = [col1, col2, col3, col4, col5]
    k = 0
    for i in range(0,6):
        for j in range(1,6):
            with col[j-1]:
                st.text(recommended_anime[j+k])
                st.image(recommended_anime_posters[j+k])
        k = k+5