# import pickle
# import streamlit as st
# import requests

# # Function to fetch movie details
# def fetch_movie_details(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#     response = requests.get(url).json()

#     poster_path = response.get('poster_path')
#     description = response.get('overview', 'Description not available')
#     rating = response.get('vote_average', 'N/A')
#     release_date = response.get('release_date', 'Unknown')

#     # Fetch cast (top 5)
#     cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8"
#     cast_response = requests.get(cast_url).json()
#     cast = [member['name'] for member in cast_response.get('cast', [])[:5]]
#     cast_names = ', '.join(cast) if cast else 'Cast not available'

#     # Construct full poster URL
#     poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

#     return {
#         'poster_url': poster_url,
#         'description': description,
#         'rating': rating,
#         'release_date': release_date,
#         'cast': cast_names
#     }


# # Function to recommend similar movies
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

#     recommended_movies = []
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         movie_title = movies.iloc[i[0]].title
#         details = fetch_movie_details(movie_id)
#         recommended_movies.append({
#             'title': movie_title,
#             'movie_id': movie_id,
#             **details
#         })

#     return recommended_movies

# import streamlit as st

# # Apply custom background color using CSS
# st.markdown(
#     """
#     <style>
#         .stApp {
#             background: linear-gradient(135deg, #1f1f2e, #3a3a4d);
#             color: #FFFFFF;
#         }

#         section[data-testid="stSidebar"] {
#             background-color: #2c2c3d;
#         }

#         h1, h2, h3, h4, h5, h6 {
#             color: #FF6347;
#         }

#         p {
#             color: #FFFFFF;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("🎬 Movie Recommender System 🍿")
# st.write("This app recommends movies based on your selection!")


# # Streamlit UI
# st.markdown("<h1 style='text-align: center; color: #E50914;'>🎬 Movie Recommender System 🍿</h1>", unsafe_allow_html=True)

# # Load datasets
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # Dropdown for movie selection
# movie_list = movies['title'].values
# selected_movie = st.selectbox("🔍 Select a movie:", movie_list)

# # Show recommendations
# if st.button('🎯 Show Recommendations'):
#     recommended_movies = recommend(selected_movie)

#     # Display recommended movies in 5 cards
#     for movie in recommended_movies:
#         st.markdown("---")
#         # Movie card
#         st.image(movie['poster_url'], caption=movie['title'], width=300)
#         st.markdown(f"""
#             <div style='background-color: #1e1e1e; padding: 15px; border-radius: 15px;'>
#                 <h3 style='color: #FFD700;'>🎞️ {movie['title']}</h3>
#                 <p style='color: #FFFFFF;'>📝 <strong>Description:</strong> {movie['description']}</p>
#                 <p style='color: #FFFFFF;'>⭐ <strong>Rating:</strong> {movie['rating']}/10</p>
#                 <p style='color: #FFFFFF;'>🗓️ <strong>Release Date:</strong> {movie['release_date']}</p>
#                 <p style='color: #FFFFFF;'>👥 <strong>Top Cast:</strong> {movie['cast']}</p>
#             </div>
#         """, unsafe_allow_html=True)

import pickle
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load the API key from environment variable
load_dotenv()
api_key = os.getenv("API_KEY")

# Function to fetch movie details
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url).json()

    poster_path = response.get('poster_path')
    description = response.get('overview', 'Description not available')
    rating = response.get('vote_average', 'N/A')
    release_date = response.get('release_date', 'Unknown')

    # Fetch cast (top 5)
    cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
    cast_response = requests.get(cast_url).json()
    cast = [member['name'] for member in cast_response.get('cast', [])[:5]]
    cast_names = ', '.join(cast) if cast else 'Cast not available'

    # Construct full poster URL
    poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

    return {
        'poster_url': poster_url,
        'description': description,
        'rating': rating,
        'release_date': release_date,
        'cast': cast_names
    }


# Function to recommend similar movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_title = movies.iloc[i[0]].title
        details = fetch_movie_details(movie_id)
        recommended_movies.append({
            'title': movie_title,
            'movie_id': movie_id,
            **details
        })

    return recommended_movies

st.sidebar.markdown("<h1 style='text-align: center; color: #E50914;'>🎬 Movie Recommending System 🍿</h1>", unsafe_allow_html=True)

# Load datasets
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown for movie selection in sidebar
movie_list = movies['title'].values
selected_movie = st.sidebar.selectbox("🔍 Select a movie:", movie_list)

# Show recommendations
if st.sidebar.button('🎯 Show Recommendations'):
    recommended_movies = recommend(selected_movie)

    # Display recommended movies in 5 cards
    for movie in recommended_movies:
        st.markdown("---")
        st.image(movie['poster_url'], caption=movie['title'], width=300)
        st.markdown(f"""
            <div style='background-color: #1e1e1e; padding: 15px; border-radius: 15px;'>
                <h3 style='color: #FFD700;'>🎞️ {movie['title']}</h3>
                <p style='color: #FFFFFF;'>📝 <strong>Description:</strong> {movie['description']}</p>
                <p style='color: #FFFFFF;'>⭐ <strong>Rating:</strong> {movie['rating']}/10</p>
                <p style='color: #FFFFFF;'>🗓️ <strong>Release Date:</strong> {movie['release_date']}</p>
                <p style='color: #FFFFFF;'>👥 <strong>Top Cast:</strong> {movie['cast']}</p>
            </div>
        """, unsafe_allow_html=True) 

st.sidebar.info("Select a movie from the dropdown and click 'Show Recommendations' to get personalized movie suggestions.")
