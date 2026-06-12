import pickle
import requests
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# Load data
df = pickle.load(open("df.pkl", "rb"))
indices = pickle.load(open("indices.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))

# 🎬 Fetch poster + rating
@st.cache_data
def fetch_movie_data(movie_name):
    try:
        url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}"
        data = requests.get(url).json()

        if data.get("Response") == "True":
            poster = data.get("Poster")
            rating = data.get("imdbRating")

            if poster == "N/A":
                poster = None

            return poster, rating

        return None, None

    except:
        return None, None


# 🔥 Fetch Trending Movies
@st.cache_data
def fetch_trending_movies():

    try:

        url = (
            f"https://api.themoviedb.org/3/trending/movie/day"
            f"?api_key={TMDB_API_KEY}"
        )

        data = requests.get(url).json()

        movies = []

        if "results" in data:

            for movie in data["results"][:10]:

                title = movie.get("title")

                poster_path = movie.get("poster_path")

                rating = movie.get("vote_average")

                if poster_path:
                    poster = (
                        "https://image.tmdb.org/t/p/w500"
                        + poster_path
                    )
                else:
                    poster = None

                trailer = fetch_trailer(title)

                movies.append({
                    "title": title,
                    "poster": poster,
                    "rating": rating,
                    "trailer": trailer
                })

        return movies

    except Exception as e:

        print(e)

        return []



# 🎞 Fetch trailer
@st.cache_data
def fetch_trailer(movie_name):

    # -----------------------------
    # FIRST TRY → TMDB
    # -----------------------------

    try:

        tmdb_url = (
            f"https://api.themoviedb.org/3/search/movie"
            f"?api_key={TMDB_API_KEY}"
            f"&query={movie_name}"
        )

        tmdb_data = requests.get(tmdb_url).json()

        if tmdb_data.get("results"):

            movie_id = tmdb_data["results"][0]["id"]

            video_url = (
                f"https://api.themoviedb.org/3/movie/"
                f"{movie_id}/videos"
                f"?api_key={TMDB_API_KEY}"
            )

            video_data = requests.get(video_url).json()

            if video_data.get("results"):

                for video in video_data["results"]:

                    if (
                        video["site"] == "YouTube"
                        and video["type"] in ["Trailer", "Teaser"]
                    ):

                        return (
                            "https://www.youtube.com/watch?v="
                            + video["key"]
                        )

    except Exception as e:
        print("TMDB Error:", e)

    # -----------------------------
    # SECOND TRY → YOUTUBE SEARCH
    # -----------------------------

    try:

        query = f"{movie_name} official trailer"

        youtube_url = (
            "https://www.googleapis.com/youtube/v3/search"
            f"?part=snippet"
            f"&q={query}"
            f"&type=video"
            f"&videoEmbeddable=true"
            f"&maxResults=5"
            f"&key={YOUTUBE_API_KEY}"
        )

        youtube_data = requests.get(youtube_url).json()

        if youtube_data.get("items"):

            for item in youtube_data["items"]:

                title = item["snippet"]["title"].lower()

                if (
                    "official" in title
                    or "trailer" in title
                ):

                    video_id = item["id"]["videoId"]

                    return (
                        "https://www.youtube.com/watch?v="
                        + video_id
                    )

            # fallback first video
            video_id = youtube_data["items"][0]["id"]["videoId"]

            return (
                "https://www.youtube.com/watch?v="
                + video_id
            )

    except Exception as e:
        print("YouTube Error:", e)

    return None

# 🎯 Recommend function
def recommend(movie, n=10):

    idx = indices[movie]

    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    movie_indices = sim_scores.argsort()[::-1][1:n+1]

    names, posters, ratings, trailers = [], [], [], []

    for i in movie_indices:

        if i >= len(df):
            continue

        title = df.iloc[i]['names']

        poster, rating = fetch_movie_data(title)
        trailer = fetch_trailer(title)

        names.append(title)
        posters.append(poster)
        ratings.append(rating)
        trailers.append(trailer)

    return names, posters, ratings, trailers