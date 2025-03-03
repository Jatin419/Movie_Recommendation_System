# import pickle
# import streamlit as st
# import requests

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:7]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters


# st.header('Movie Recommending System')
# movies = pickle.load(open('movie_list.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))

# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )

# if st.button('Show Movie Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 , col6 , col7 = st.columns(7)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
#     with col6:
#         st.text(recommended_movie_names[5])
#         st.image(recommended_movie_posters[5])
    


# import pickle
# import streamlit as st
# import requests

# # Function to fetch movie details (poster, description, cast, and rating)
# def fetch_movie_details(movie_id):
#     # TMDb API base URL with movie_id
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#     response = requests.get(url).json()

#     # Extract required details
#     poster_path = response.get('poster_path')
#     description = response.get('overview', 'Description not available')
#     rating = response.get('vote_average', 'N/A')

#     # Construct full poster URL
#     poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

#     # Fetch cast details (top 3 actors)
#     cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8"
#     cast_response = requests.get(cast_url).json()
#     cast = [member['name'] for member in cast_response.get('cast', [])[:3]]
#     cast_names = ', '.join(cast) if cast else 'Cast not available'

#     return poster_url, description, cast_names, rating


# # Function to recommend similar movies
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

#     recommended_movies = []
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         movie_title = movies.iloc[i[0]].title

#         # Fetch movie details
#         poster_url, description, cast, rating = fetch_movie_details(movie_id)
#         recommended_movies.append({
#             'title': movie_title,
#             'poster_url': poster_url,
#             'description': description,
#             'cast': cast,
#             'rating': rating
#         })

#     return recommended_movies


# # Streamlit UI
# st.header('Movie Recommender System')

# # Load the movie dataset and similarity matrix
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # Dropdown for movie selection
# movie_list = movies['title'].values
# selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# # Button to show recommendations
# if st.button('Show Recommendation'):
#     recommended_movies = recommend(selected_movie)

#     # Display recommended movies in 5 columns
#     cols = st.columns(5)
#     for idx, col in enumerate(cols):
#         if idx < len(recommended_movies):
#             movie = recommended_movies[idx]
#             with col:
#                 st.text(movie['title'])  # Movie Title
#                 if movie['poster_url']:
#                     st.image(movie['poster_url'])  # Movie Poster
#                 st.write(f"**Rating:** {movie['rating']}/10")
#                 st.write(f"**Cast:** {movie['cast']}")
#                 st.write(f"**Description:** {movie['description'][:200]}...")  # Limit to 200 chars


# import pickle
# import streamlit as st
# import requests

# # Function to fetch detailed movie information
# def fetch_movie_details(movie_id):
#     # Fetch basic movie details
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#     response = requests.get(url).json()

#     poster_path = response.get('poster_path')
#     description = response.get('overview', 'Description not available')
#     rating = response.get('vote_average', 'N/A')
#     release_date = response.get('release_date', 'Unknown')

#     # Construct full poster URL
#     poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

#     # Fetch cast details (top 5 actors)
#     cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8"
#     cast_response = requests.get(cast_url).json()
#     cast = [member['name'] for member in cast_response.get('cast', [])[:5]]
#     cast_names = ', '.join(cast) if cast else 'Cast not available'

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
#         movie_details = fetch_movie_details(movie_id)
#         recommended_movies.append({
#             'title': movie_title,
#             'movie_id': movie_id,
#             **movie_details
#         })

#     return recommended_movies


# # Streamlit UI
# st.header('🎬 Movie Recommender System')

# # Load the movie dataset and similarity matrix
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # Dropdown for movie selection
# movie_list = movies['title'].values
# selected_movie = st.selectbox("🔍 Type or select a movie:", movie_list)

# # Button to show recommendations
# if st.button('🎯 Show Recommendations'):
#     recommended_movies = recommend(selected_movie)

#     # Display recommended movies in 5 columns
#     cols = st.columns(5)
#     for idx, col in enumerate(cols):
#         if idx < len(recommended_movies):
#             movie = recommended_movies[idx]
#             with col:
#                 st.image(movie['poster_url'], caption=movie['title'], use_column_width=True)
#                 st.write(f"⭐ Rating: {movie['rating']}/10")
#                 st.write(f"🗓️ Release Date: {movie['release_date']}")
#                 st.write(f"👥 Cast: {movie['cast']}")
                
#                 # Add a button to show detailed description
#                 if st.button(f"ℹ️ View Details: {movie['title']}"):
#                     # Display detailed description in an expander
#                     with st.expander(f"🔎 {movie['title']} - Description"):
#                         st.write(f"🎬 **Title:** {movie['title']}")
#                         st.image(movie['poster_url'], width=300)
#                         st.write(f"📝 **Description:** {movie['description']}")
#                         st.write(f"⭐ **Rating:** {movie['rating']}/10")
#                         st.write(f"🗓️ **Release Date:** {movie['release_date']}")
#                         st.write(f"👥 **Top Cast:** {movie['cast']}")
import pickle
import streamlit as st
import requests

# Function to fetch movie details
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url).json()

    poster_path = response.get('poster_path')
    description = response.get('overview', 'Description not available')
    rating = response.get('vote_average', 'N/A')
    release_date = response.get('release_date', 'Unknown')

    # Fetch cast (top 5)
    cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8"
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

# Streamlit UI
st.sidebar.markdown("<h1 style='text-align: center; color: #E50914;'>🎬 Movie Recommender System 🍿</h1>", unsafe_allow_html=True)

# Load datasets
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.sidebar.selectbox("🔍 Select a movie:", movie_list)

# Show recommendations
if st.sidebar.button('🎯 Show Recommendations'):
    recommended_movies = recommend(selected_movie)

    # Display recommended movies with poster and details side-by-side
    for movie in recommended_movies:
        st.markdown("---")
        col1, col2= st.columns([1, 2])
        with col1:
            
            
            st.image(movie['poster_url'], caption=movie['title'], width=300)
        with col2:
            st.markdown(f"""
                        
                <div style='background-color: #1e1e1e; padding: 15px; border-radius: 15px;'>
                    <h3 style='color: #FFD700;'>🎞️ {movie['title']}</h3>
                    <p style='color: #FFFFFF;'>📝 <strong>Description:</strong> {movie[  'description']}</p>
                    <p style='color: #FFFFFF;'>⭐ <strong>Rating:</strong> {movie[  'rating']}/10</p>
                    <p style='color: #FFFFFF;'>🗓️ <strong>Release Date:</strong> {movie[  'release_date']}</p>
                    <p style='color: #FFFFFF;'>👥 <strong>Top Cast:</strong> {movie[  'cast']}</p>
                </div>
                
                
            """, unsafe_allow_html=True)
