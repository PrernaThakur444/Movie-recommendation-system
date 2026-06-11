import streamlit as st
import pickle

from auth import (
    add_favorite,
    add_watch_history,
    get_favorites,
    get_watch_history,
    register_user,
    login_user,
    remove_favorite,
    remove_watch_history
)

from main import (
    recommend,
    fetch_movie_data,
    fetch_trailer,
    fetch_trending_movies
)

from smart_search import smart_search


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Movie Recommender",
    layout="wide"
)


# ==========================================
# LOAD DATA
# ==========================================

df = pickle.load(open("df.pkl", "rb"))


# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "trailer" not in st.session_state:
    st.session_state.trailer = None


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* =========================
   MAIN BACKGROUND
========================= */

.stApp {

    background:
        linear-gradient(
            to bottom,
            #0f0f0f,
            #1c1c1c
        );

    color: white;
}


/* =========================
   LIGHT MODE SUPPORT
========================= */

@media (prefers-color-scheme: light) {

    .stApp {

        background: #f5f5f5;
        color: #111111;
    }

    h1, h2, h3, h4, h5, h6 {

        color: #111111 !important;
    }

    p, span, label, div {

        color: #222222 !important;
    }

    .stButton button {

        background-color: white !important;
        color: black !important;
    }
}


/* =========================
   TITLES
========================= */

h1, h2, h3 {

    font-weight: bold;
}


/* =========================
   MOVIE POSTERS
========================= */

img {

    border-radius: 20px;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.5);

    transition: 0.4s ease;

    cursor: pointer;
}

img:hover {

    transform:
        scale(1.05)
        translateY(-5px);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.7);
}


/* =========================
   BUTTONS
========================= */

.stButton button {

    width: 100%;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.15),
            rgba(255,255,255,0.05)
        );

    color: white !important;

    border:
        1px solid rgba(255,255,255,0.2);

    padding: 10px;

    transition: 0.3s ease;
}

.stButton button:hover {

    transform: scale(1.05);

    background:
        linear-gradient(
            135deg,
            #ff416c,
            #ff4b2b
        );
}


/* =========================
   INPUT BOXES
========================= */

.stTextInput input {

    border-radius: 12px !important;
}


/* =========================
   SPACING
========================= */

[data-testid="column"] {

    padding: 10px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LOGIN PAGE
# ==========================================

if not st.session_state.logged_in:

    st.title("🔐 Login")

    auth_option = st.radio(
        "Choose Option",
        ["Login", "Register"]
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    # LOGIN
    if auth_option == "Login":

        if st.button("Login"):

            success = login_user(
                username,
                password
            )

            if success:

                st.session_state.logged_in = True

                st.session_state.username = username

                st.rerun()

            else:

                st.error(
                    "Invalid Username or Password"
                )

    # REGISTER
    else:

        if st.button("Register"):

            if register_user(username, password):

                st.success(
                    "Registration Successful"
                )

            else:

                st.error(
                    "User already exists"
                )

    st.stop()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.success(
    f"Logged in as {st.session_state.username}"
)

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.session_state.username = ""

    st.rerun()


# ==========================================
# MAIN TITLE
# ==========================================

st.title("🎬 Movie Recommender")

st.write(
    "Unlimited movies, recommendations and trailers 🍿"
)


# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
    <div style="
    background: linear-gradient(to right, rgba(0,0,0,0.9), rgba(0,0,0,0.1)),
    url('https://image.tmdb.org/t/p/original/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg');
    background-size: cover;
    padding: 60px;
    border-radius: 10px;
    color: white;
    ">
    <h1 style="font-size:50px;">Discover Movies You'll Love</h1>
    <p>AI-powered recommendations just for you</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# SEARCH SECTION
# ==========================================

st.markdown("---")

search_query = st.text_input(
    "🔍 Search Movie"
)

matches = []

if search_query:

    matches = smart_search(
        search_query,
        top_n=5
    )

selected_movie = None

for i, movie in enumerate(matches):

    if st.button(movie, key=f"search_{i}"):

        selected_movie = movie

if selected_movie:

    st.session_state.selected = selected_movie


# ==========================================
# RECOMMENDATIONS
# ==========================================

if "selected" in st.session_state:

    st.markdown("## 🔥 Recommended for You")

    names, posters, ratings, trailers = recommend(
        st.session_state.selected,
        10
    )

    cols = st.columns(5)

    for i in range(len(names)):

        with cols[i % 5]:

            if posters[i]:

                st.image(posters[i], width=200)

            st.write(names[i])

            if ratings[i] != "N/A":

                st.write(f"⭐ {ratings[i]}")

            # FAVORITE
            if st.button(
                "❤️ Favorite",
                key=f"fav_{i}"
            ):

                add_favorite(
                    st.session_state.username,
                    names[i],
                    posters[i]
                )

                st.success(
                    "Added to Favorites"
                )

            # PLAY
            if st.button(
                "▶ Play",
                key=f"play_{i}"
            ):

                add_watch_history(
                    st.session_state.username,
                    names[i],
                    posters[i]
                )

                if trailers[i]:

                    st.session_state.trailer = trailers[i]

                else:

                    st.warning(
                        "Trailer not available"
                    )

        if (i + 1) % 5 == 0:

            cols = st.columns(5)


# ==========================================
# MOOD-BASED RECOMMENDATION
# ==========================================

st.markdown("---")
st.markdown("## 😊 Choose Your Mood")

mood_to_genre = {

    "😊 Happy": "Comedy",
    "😢 Emotional": "Drama",
    "😍 Romantic": "Romance",
    "😨 Thriller": "Thriller",
    "🤯 Mind-Bending": "Sci-Fi",
    "😎 Chill": "Adventure"
}

mood_cols = st.columns(len(mood_to_genre))

selected_mood = None

for i, mood in enumerate(mood_to_genre.keys()):

    with mood_cols[i]:

        if st.button(mood):

            selected_mood = mood

if selected_mood:

    genre = mood_to_genre[selected_mood]

    st.markdown(f"## 🎬 {selected_mood} Movies")

    mood_movies = df[
        df['genre'].str.contains(
            genre,
            case=False,
            na=False
        )
    ].head(10)

    cols = st.columns(5)

    for i, row in enumerate(mood_movies.itertuples()):

        movie_name = row.names

        poster, rating = fetch_movie_data(
            movie_name
        )

        trailer = fetch_trailer(movie_name)

        with cols[i % 5]:

            if poster:

                st.image(poster, width=200)

            st.write(movie_name)

            st.write(f"⭐ {rating}")

            if st.button(
                "❤️ Favorite",
                key=f"mood_fav_{i}"
            ):

                add_favorite(
                    st.session_state.username,
                    movie_name,
                    poster
                )

            if st.button(
                "▶ Play",
                key=f"mood_play_{i}"
            ):

                if trailer:

                    st.session_state.trailer = trailer

                    add_watch_history(
                        st.session_state.username,
                        movie_name,
                        poster
                    )

                else:

                    st.warning(
                        "Trailer not available"
                    )

        if (i + 1) % 5 == 0:

            cols = st.columns(5)


# ==========================================
# TRENDING MOVIES
# ==========================================

st.markdown("---")
st.markdown("## 🔥 Trending Today")

trending_movies = fetch_trending_movies()

if trending_movies:

    cols = st.columns(5)

    for i, movie in enumerate(trending_movies):

        with cols[i % 5]:

            if movie["poster"]:

                st.image(
                    movie["poster"],
                    width=200
                )

            st.write(movie["title"])

            st.write(
                f"⭐ {movie['rating']}"
            )

            if st.button(
                "▶ Play",
                key=f"trend_{i}"
            ):

                if movie["trailer"]:

                    st.session_state.trailer = movie["trailer"]

                else:

                    st.warning(
                        "Trailer not available"
                    )

        if (i + 1) % 5 == 0:

            cols = st.columns(5)

else:

    st.warning(
        "Trending movies not loading"
    )


# ==========================================
# FAVORITES
# ==========================================

st.markdown("---")
st.markdown("## ❤️ My Favorite Movies")

favorites = get_favorites(
    st.session_state.username
)

if favorites:

    cols = st.columns(5)

    for i, movie in enumerate(favorites):

        with cols[i % 5]:

            if movie[1]:

                st.image(movie[1], width=200)

            st.write(movie[0])

            if st.button(
                "❌ Remove",
                key=f"remove_{i}"
            ):

                remove_favorite(
                    st.session_state.username,
                    movie[0]
                )

                st.rerun()

        if (i + 1) % 5 == 0:

            cols = st.columns(5)

else:

    st.info("No favorite movies yet")


# ==========================================
# WATCH HISTORY
# ==========================================

st.markdown("---")
st.markdown("## 📜 Recently Watched")

history = get_watch_history(
    st.session_state.username
)

if history:

    cols = st.columns(5)

    for i, movie in enumerate(history[:10]):

        with cols[i % 5]:

            if movie[1]:

                st.image(movie[1], width=200)

            st.write(movie[0])

            if st.button(
                "❌ Remove",
                key=f"history_remove_{i}"
            ):

                remove_watch_history(
                    st.session_state.username,
                    movie[0]
                )

                st.rerun()

        if (i + 1) % 5 == 0:

            cols = st.columns(5)

else:

    st.info("No watch history yet")


# ==========================================
# GENRE SECTION
# ==========================================

st.markdown("---")
st.markdown("## 🎭 Browse by Genre")


def show_genre_row(genre_name):

    st.markdown(f"### {genre_name}")

    filtered = df[
        df['genre'].str.contains(
            genre_name,
            case=False,
            na=False
        )
    ].head(10)

    cols = st.columns(5)

    for i, row in enumerate(filtered.itertuples()):

        movie_name = row.names

        poster, rating = fetch_movie_data(
            movie_name
        )

        trailer = fetch_trailer(movie_name)

        with cols[i % 5]:

            if poster:

                st.image(poster, width=200)

            st.write(movie_name)

            st.write(f"⭐ {rating}")

            if st.button(
                "▶ Play",
                key=f"{genre_name}_{i}"
            ):

                if trailer:

                    st.session_state.trailer = trailer

                else:

                    st.warning(
                        "Trailer not available"
                    )

        if (i + 1) % 5 == 0:

            cols = st.columns(5)


show_genre_row("Action")
show_genre_row("Comedy")
show_genre_row("Drama")


# ==========================================
# VIDEO PLAYER
# ==========================================

if st.session_state.trailer:

    st.markdown("---")
    st.markdown("## 🎬 Now Playing")

    embed_url = (
        st.session_state.trailer
        .replace("watch?v=", "embed/")
    )

    st.video(embed_url)

    if st.button("⛔ Stop Trailer"):

        st.session_state.trailer = None

        st.rerun()