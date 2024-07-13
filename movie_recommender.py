import pickle
import streamlit as st
import requests

# Set the page configuration to use the wide layout
st.set_page_config(layout="wide")

# Loading web app in localhost
st.header("Movie Recommendation System")
st.text("Get the movie which matches your taste! Add it to your watchlist, hurry up :)")

# Load data and models
with open("C:/Users/aksha/OneDrive/Desktop/recommendation_system/movie_list.pkl", 'rb') as file:
    movies = pickle.load(file)

with open('C:/Users/aksha/OneDrive/Desktop/recommendation_system/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('C:/Users/aksha/OneDrive/Desktop/recommendation_system/nn.pkl', 'rb') as file:
    nn_model = pickle.load(file)

with open("C:/Users/aksha/OneDrive/Desktop/recommendation_system/posters.pkl", 'rb') as file:
    posters = pickle.load(file)

movie_list = movies['title'].values
selected_movie = st.selectbox('Type the Movie Name for recommendation', movie_list)

# Fetch poster function
def fetch_poster(movie_id):
    path = posters.loc[posters['id'] == movie_id,'poster_path'].values[0]
    fullpath = "https://image.tmdb.org/t/p/w500" + path
    return fullpath

# Recommend function
def recommend(movie):
    similar_movies = []
    similar_posters = []
    
    # Find the index of the selected movie
    idx = movies.index[movies['title'] == movie].tolist()[0]
    # Transform the tags of the selected movie
    movie_tags_tfidf = vectorizer.transform([movies.loc[idx, 'tags']])
    
    # Ensure n_neighbors is valid
    n_neighbors = min(15, movies.shape[0])  
    
    # Get nearest neighbors
    distances, indices = nn_model.kneighbors(movie_tags_tfidf, n_neighbors=n_neighbors)
    
    # Exclude the first result (it is the movie itself)
    recommended_indices = indices.flatten()[1:]
    recommended_movies = movies.iloc[recommended_indices]
    
    for i in range(len(recommended_movies)):
        movie_id = recommended_movies.iloc[i]['id']
        movie_title = recommended_movies.iloc[i]['title']
        similar_movies.append(movie_title)
        similar_posters.append(fetch_poster(movie_id))
    
    return similar_movies, similar_posters

# Filter button
if st.button('Similar Movies'):
    similar_movies, movie_posters = recommend(selected_movie)
    for i in range(0, 10, 5):  # Adjust range as needed
        cols = st.columns(5)
        for j, col in enumerate(cols):
            if i + j < len(similar_movies):
                with col:
                    st.text(similar_movies[i + j])
                    st.image(movie_posters[i + j])
