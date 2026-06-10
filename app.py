# # import streamlit as st
# # import pickle
# # from main import recommend

# # # Load dataframe
# # df = pickle.load(open("df.pkl", "rb"))

# # # Page config
# # st.set_page_config(page_title="Movie Recommender", layout="wide")

# # # 🎨 Custom UI Styling
# # st.markdown("""
# # <style>

# # .stApp {
# #     background-color: pink;
# # }

# # h1 {
# #     color: black;
# #     text-align: center;
# # }

# # .movie-title {
# #     color: black;
# #     font-weight: bold;
# #     text-align: center;
# #     font-size: 14px;
# # }

# # .rating {
# #     color: #FF9900;
# #     text-align: center;
# #     font-size: 13px;
# # }

# # .card {
# #     background-color: black;
# #     padding: 10px;
# #     border-radius: 10px;
# #     box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
# #     text-align: center;
# #     margin-bottom: 10px;
# # }

# # </style>
# # """, unsafe_allow_html=True)

# # # Title
# # st.title("🎬 Movie Recommendation System")

# # st.write("Select a movie and get similar recommendations with posters and ratings.")

# # # Movie selection
# # selected_movie = st.selectbox(
# #     "Choose a movie",
# #     df['names'].values
# # )

# # # Recommend button
# # if st.button("Recommend"):

# #     names, posters, ratings = recommend(selected_movie, 10)

# #     cols = st.columns(5)

# #     for i in range(len(names)):

# #         with cols[i % 5]:

# #             st.markdown('<div class="card">', unsafe_allow_html=True)

# #             if posters[i]:
# #                 st.image(posters[i], use_container_width=True)

# #             st.markdown(f'<div class="movie-title">{names[i]}</div>', unsafe_allow_html=True)

# #             if ratings[i] and ratings[i] != "N/A":
# #                 st.markdown(f'<div class="rating">⭐ {ratings[i]}</div>', unsafe_allow_html=True)

# #             st.markdown('</div>', unsafe_allow_html=True)

# #         if (i + 1) % 5 == 0 and i != len(names) - 1:
# #             cols = st.columns(5)



# import streamlit as st
# import pickle
# from main import recommend

# # Load data
# df = pickle.load(open("df.pkl", "rb"))

# st.set_page_config(page_title="Movie Recommender", layout="wide")

# # 🎨 Netflix Style CSS
# st.markdown("""
# <style>

# .stApp {
#     background-color: #141414;
# }

# /* Title */
# h1 {
#     color: #E50914;
#     text-align: center;
#     font-size: 40px;
# }

# /* Search box */
# input {
#     background-color: #1f1f1f !important;
#     color: white !important;
# }

# /* Card */
# .card {
#     background-color: #1f1f1f;
#     padding: 10px;
#     border-radius: 8px;
#     text-align: center;
#     transition: 0.3s;
# }

# /* Hover effect */
# .card:hover {
#     transform: scale(1.08);
#     box-shadow: 0px 4px 20px rgba(229, 9, 20, 0.6);
# }

# /* Movie title */
# .movie-title {
#     color: white;
#     font-size: 14px;
#     margin-top: 5px;
# }

# /* Rating */
# .rating {
#     color: #B3B3B3;
#     font-size: 13px;
# }

# /* Button */
# .stButton>button {
#     background-color: #E50914;
#     color: white;
#     border-radius: 5px;
# }

# </style>
# """, unsafe_allow_html=True)

# # Title
# st.title("🎬 Movie Recommender")

# st.write("Search for a movie and explore similar recommendations 🍿")

# # 🔍 Autocomplete search
# search_query = st.text_input("Search movie")

# matches = df[df['names'].str.lower().str.contains(search_query.lower())]['names'].head(5)

# selected_movie = None

# if search_query:
#     for i, movie in enumerate(matches):
#         if st.button(movie, key=f"search_{i}"):
#          selected_movie = movie

# # Store selection
# if selected_movie:
#     st.session_state["selected"] = selected_movie

# # Show recommendations
# if "selected" in st.session_state:

#     names, posters, ratings, trailers = recommend(st.session_state["selected"], 10)

#     cols = st.columns(5)

#     for i in range(len(names)):

#         with cols[i % 5]:

#             st.markdown('<div class="card">', unsafe_allow_html=True)

#             if posters[i]:
#                 st.image(posters[i], width='stretch')

#             st.markdown(f'<div class="movie-title">{names[i]}</div>', unsafe_allow_html=True)

#             if ratings[i] and ratings[i] != "N/A":
#                 st.markdown(f'<div class="rating">⭐ {ratings[i]}</div>', unsafe_allow_html=True)

#             # 🎞 Click-to-play trailer
#             st.markdown(f"[▶ Watch Trailer]({trailers[i]})")

#             st.markdown('</div>', unsafe_allow_html=True)

#         if (i + 1) % 5 == 0 and i != len(names) - 1:
#             cols = st.columns(5)



# import streamlit as st
# import pickle
# from main import recommend

# df = pickle.load(open("df.pkl", "rb"))

# st.set_page_config(page_title="Movie Recommender", layout="wide")

# # 🎨 Netflix UI
# st.markdown("""
# <style>

# /* Background */
# .stApp {
#     background-color: #000000;
# }

# /* Title */
# h1 {
#     color: #E50914;
#     text-align: center;
#     font-size: 48px;
#     font-weight: bold;
# }

# /* Subtitle text */
# p {
#     color: #ffffff;
#     text-align: center;
# }

# /* Search box */
# input {
#     background-color: #141414 !important;
#     color: white !important;
#     border: 1px solid #333 !important;
# }

# /* Movie card */
# .card {
#     background-color: #141414;
#     padding: 10px;
#     border-radius: 6px;
#     text-align: center;
#     transition: transform 0.3s ease;
# }

# /* Hover effect */
# .card:hover {
#     transform: scale(1.12);
#     z-index: 10;
# }

# /* Movie title */
# .movie-title {
#     color: #ffffff;
#     font-size: 14px;
#     margin-top: 5px;
#     font-weight: 500;
# }

# /* Rating */
# .rating {
#     color: #aaa;
#     font-size: 13px;
# }

# /* Buttons */
# .stButton>button {
#     background-color: #E50914;
#     color: white;
#     border: none;
#     border-radius: 4px;
#     padding: 5px 10px;
# }

# /* Button hover */
# .stButton>button:hover {
#     background-color: #f40612;
# }

# </style>
# """, unsafe_allow_html=True)

# st.title("🎬 Movie Recommender")

# # 🔍 Search
# search_query = st.text_input("Search movie")

# matches = df[df['names'].str.lower().str.contains(search_query.lower())]['names'].head(5)

# selected_movie = None

# if search_query:
#     for i, movie in enumerate(matches):
#         if st.button(movie, key=f"search_{i}"):
#             selected_movie = movie

# # Save selection
# if selected_movie:
#     st.session_state["selected"] = selected_movie

# # 🎬 Show recommendations
# if "selected" in st.session_state:

#     names, posters, ratings, trailers = recommend(st.session_state["selected"], 10)

#     cols = st.columns(5)

#     for i in range(len(names)):

#         with cols[i % 5]:

#             st.markdown('<div class="card">', unsafe_allow_html=True)

#             if posters[i]:
#                 st.image(posters[i], width='stretch')

#             st.markdown(f'<div class="movie-title">{names[i]}</div>', unsafe_allow_html=True)

#             if ratings[i] and ratings[i] != "N/A":
#                 st.markdown(f'<div class="rating">⭐ {ratings[i]}</div>', unsafe_allow_html=True)

#             # 🎞 Play trailer inside app
#             if st.button(f"▶ Trailer {i}", key=f"trailer_{i}"):

#                 if trailers[i]:
#                     st.video(trailers[i])
#                 else:
#                     st.write("Trailer not available")

#             st.markdown('</div>', unsafe_allow_html=True)

#         if (i + 1) % 5 == 0 and i != len(names) - 1:
#             cols = st.columns(5)


# import streamlit as st
# from auth import add_favorite, add_watch_history, get_favorites, get_watch_history, register_user, login_user, remove_favorite, remove_watch_history
# import pickle
# from main import recommend, fetch_movie_data, fetch_trailer, fetch_trending_movies
# from smart_search import smart_search

# st.set_page_config(page_title="Movie Recommender", layout="wide")
# # Load data
# df = pickle.load(open("df.pkl", "rb"))



# # 🎯 SESSION STATE
# if "trailer" not in st.session_state:
#     st.session_state.trailer = None

# # LOGIN SESSION
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if "username" not in st.session_state:
#     st.session_state.username = ""


# # if "logged_in" not in st.session_state:
# #     st.session_state.logged_in = False

# # if "username" not in st.session_state:
# #     st.session_state.username = ""

# # if "trailer" not in st.session_state:
# #     st.session_state.trailer = None    




# # 🎨 UI
# # st.markdown("""
# # <style>
# # .stApp { background-color: #000000; }

# # h1 {
# #     color: #E50914;
# #     text-align: center;
# #     font-size: 48px;
# # }

# # input {
# #     background-color: #141414 !important;
# #     color: white !important;
# # }
# # </style>
# # """, unsafe_allow_html=True)

# st.markdown("""
# <style>

# /* =========================
#    MAIN APP BACKGROUND
# ========================= */

# .stApp {

#     background: linear-gradient(
#         to bottom,
#         #111111,
#         #1a1a1a
#     );

#     color: white;
# }


# /* =========================
#    LIGHT MODE SUPPORT
# ========================= */

# @media (prefers-color-scheme: light) {

#     .stApp {

#         background: #f5f5f5;
#         color: #111111;
#     }

#     h1, h2, h3, h4, h5, h6 {

#         color: #111111 !important;
#     }

#     p, span, label, div {

#         color: #222222 !important;
#     }

#     .movie-title {

#         color: #111111 !important;
#     }

#     .stMarkdown {

#         color: #111111 !important;
#     }

#     .stTextInput input {

#         background-color: white !important;
#         color: black !important;
#         border: 1px solid #ccc !important;
#     }

#     .stButton button {

#         background-color: #ffffff !important;
#         color: black !important;
#         border: 1px solid #ccc !important;
#     }
# }


# /* =========================
#    DARK MODE
# ========================= */

# @media (prefers-color-scheme: dark) {

#     h1, h2, h3, h4, h5, h6 {

#         color: white !important;
#     }

#     p, span, label, div {

#         color: #dddddd !important;
#     }

#     .stTextInput input {

#         background-color: #1f1f1f !important;
#         color: white !important;
#         border: 1px solid #444 !important;
#     }

#     .stButton button {

#         background-color: #222222 !important;
#         color: white !important;
#         border: 1px solid #555 !important;
#     }
# }


# /* =========================
#    TITLE
# ========================= */

# h1 {

#     text-align: center;
#     font-size: 48px;
#     font-weight: bold;
# }


# /* =========================
#    MOVIE POSTER EFFECT
# ========================= */

# img {

#     border-radius: 10px;
#     transition: 0.3s;
# }

# img:hover {

#     transform: scale(1.03);
# }


# /* =========================
#    BUTTON STYLE
# ========================= */

# .stButton button {

#     border-radius: 8px;
#     padding: 8px 16px;
#     transition: 0.3s;
# }

# .stButton button:hover {

#     transform: scale(1.05);
# }



# /* =========================
#    MOVIE POSTERS
# ========================= */

# img {

#     border-radius: 18px;

#     box-shadow:
#         0 10px 35px rgba(0,0,0,0.6);

#     transition: all 0.4s ease;

#     cursor: pointer;
# }


# /* =========================
#    POSTER HOVER EFFECT
# ========================= */

# img:hover {

#     transform:
#         scale(1.08)
#         translateY(-8px);

#     box-shadow:
#         0 20px 45px rgba(0,0,0,0.8);

#     filter: brightness(1.1);
# }


# /* =========================
#    MOVIE TITLES
# ========================= */

# h1, h2, h3 {

#     font-weight: 700;
# }


# /* =========================
#    BUTTON STYLE
# ========================= */

# .stButton button {

#     width: 100%;

#     border-radius: 12px;

#     background:
#         linear-gradient(
#             135deg,
#             rgba(255,255,255,0.15),
#             rgba(255,255,255,0.05)
#         );

#     color: white !important;

#     border:
#         1px solid rgba(255,255,255,0.2);

#     backdrop-filter: blur(10px);

#     padding: 10px;

#     font-weight: bold;

#     transition: all 0.3s ease;

#     box-shadow:
#         0 4px 15px rgba(0,0,0,0.4);
# }


# /* =========================
#    BUTTON HOVER
# ========================= */

# .stButton button:hover {

#     transform:
#         scale(1.05)
#         translateY(-2px);

#     background:
#         linear-gradient(
#             135deg,
#             #ff416c,
#             #ff4b2b
#         );

#     border: none;

#     box-shadow:
#         0 8px 25px rgba(255,75,43,0.5);
# }


# /* =========================
#    SECTION HEADINGS
# ========================= */

# h2 {

#     margin-top: 20px;

#     margin-bottom: 20px;

#     font-size: 42px;

#     letter-spacing: 1px;
# }


# /* =========================
#    MOVIE GRID SPACING
# ========================= */

# [data-testid="column"] {

#     padding: 10px;
# }


            

# /* =========================
#    SECTION SPACING
# ========================= */

# section.main > div {

#     padding-top: 1rem;
# }

# </style>
# """, unsafe_allow_html=True)

# # =========================================
# # LOGIN / SIGNUP SECTION
# # =========================================

# menu = ["Login", "Signup"]

# choice = st.sidebar.selectbox(
#     "Menu",
#     menu
# )

# # SIGNUP
# if choice == "Signup":

#     st.subheader("Create Account")

#     new_user = st.text_input("Username")

#     new_password = st.text_input(
#         "Password",
#         type="password"
#     )

#     if st.button("Signup"):

#         success = register_user(
#             new_user,
#             new_password
#         )

#         if success:
#             st.success("Account Created Successfully")
#         else:
#             st.error("Username already exists")


# # LOGIN
# elif choice == "Login":

#     st.subheader("Login")

#     username = st.text_input("Username")

#     password = st.text_input(
#         "Password",
#         type="password"
#     )

#     if st.button("Login"):

#         result = login_user(
#             username,
#             password
#         )

#         # if result:

#         #     st.session_state.logged_in = True
#         #     st.session_state.username = username

#         #     st.success(f"Welcome {username}")
#         if result:

#             st.session_state.logged_in = True
#             st.session_state.username = username

#             st.rerun()

#         else:
#             st.error("Invalid Credentials")
# if not st.session_state.logged_in:
#     st.stop() 

# # LOGOUT
# if st.session_state.logged_in:

#     st.sidebar.success(
#         f"Logged in as {st.session_state.username}"
#     )

#     if st.sidebar.button("Logout"):

#         st.session_state.logged_in = False
#         st.session_state.username = ""

#         st.rerun()

# if st.session_state.logged_in:


# # # ==========================================
# # # LOGIN SYSTEM
# # # ==========================================

# # if not st.session_state.logged_in:

# #     st.title("🔐 Welcome to Movie Recommender")

# #     auth_option = st.radio(
# #         "Choose Option",
# #         ["Login", "Register"]
# #     )

# #     username = st.text_input("Username")

# #     password = st.text_input(
# #         "Password",
# #         type="password"
# #     )


# #     # LOGIN
    
# #     # LOGIN
# #     if auth_option == "Login":

# #         if st.button("Login"):

# #             success = login_user(username, password)

# #             if success:

# #                 st.session_state.logged_in = True

# #                 st.session_state.username = username

# #                 st.success("Login Successful")

# #                 st.rerun()

# #             else:

# #                 st.error("Invalid Username or Password")

# #     # REGISTER
# #     else:

# #         if st.button("Register"):

# #             if register_user(username, password):

# #                 st.success("Registration Successful")

# #             else:

# #                 st.error("User already exists")


# #         # STOP APP HERE
# #         st.stop()



#     # 🎬 Title
#     st.title("🎬 Movie Recommender")
#     st.write("Unlimited movies, recommendations and trailers 🍿")

#     # 🎬 Hero Banner
#     st.markdown("""
#     <div style="
#     background: linear-gradient(to right, rgba(0,0,0,0.9), rgba(0,0,0,0.1)),
#     url('https://image.tmdb.org/t/p/original/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg');
#     background-size: cover;
#     padding: 60px;
#     border-radius: 10px;
#     color: white;
#     ">
#     <h1 style="font-size:50px;">Discover Movies You'll Love</h1>
#     <p>AI-powered recommendations just for you</p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("---")
#     # 🔍 Search
#     search_query = st.text_input("Search movie")

#     matches = []

#     if search_query:

#         matches = smart_search(
#             search_query,
#             top_n=5
#         )

#     selected_movie = None

#     if search_query:
#         for i, movie in enumerate(matches):
#             if st.button(movie, key=f"search_{i}"):
#                 selected_movie = movie

#     if selected_movie:
#         st.session_state["selected"] = selected_movie
    
#      # 🎯 Recommendations
#     if "selected" in st.session_state:

#         st.markdown("## 🔥 Recommended for You")

#         names, posters, ratings, trailers = recommend(st.session_state["selected"], 10)

#         cols = st.columns(5)

#         for i in range(len(names)):

#             with cols[i % 5]:

#                 if posters[i]:
#                     st.image(posters[i], width=200)

#                 st.write(names[i])

#                 if ratings[i] and ratings[i] != "N/A":
#                     st.write(f"⭐ {ratings[i]}")

#                 # ❤️ Favorite Button
#                 if st.button("❤️ Favorite", key=f"fav_{i}"):

#                     add_favorite(
#                         st.session_state.username,
#                         names[i],
#                         posters[i]
#                     )

#                     st.success("Added to Favorites")    

#                 if st.button("▶ Play", key=f"rec_{i}"):

#                     # Save watch history
#                     add_watch_history(
#                         st.session_state.username,
#                         names[i],
#                         posters[i]
#                     )

#                     # Play trailer
#                     if trailers[i]:

#                         st.session_state.trailer = trailers[i]

#                     else:
#                         st.warning("Trailer not available")

#         if (i + 1) % 5 == 0:
#             cols = st.columns(5)

#     st.markdown("---")

#     # ==========================================
#     # 😊 MOOD-BASED RECOMMENDATION
#     # ==========================================

#     st.markdown("## 😊 Choose Your Mood")

#     # Mood → Genre Mapping
#     mood_to_genre = {

#         "😊 Happy": "Comedy",

#         "😢 Emotional": "Drama",

#         "😍 Romantic": "Romance",

#         "😨 Thriller": "Thriller",

#         "🤯 Mind-Bending": "Sci-Fi",

#         "😎 Chill": "Adventure"
#     }


#     # Create mood buttons
#     mood_cols = st.columns(len(mood_to_genre))

#     selected_mood = None

#     for i, mood in enumerate(mood_to_genre.keys()):

#         with mood_cols[i]:

#             if st.button(mood):

#                 selected_mood = mood


#     # Show Recommendations
#     if selected_mood:

#         genre = mood_to_genre[selected_mood]

#         st.markdown(f"## 🎬 {selected_mood} Movies")


#         mood_movies = df[
#             df['genre'].str.contains(
#                 genre,
#                 case=False,
#                 na=False
#             )
#         ].head(10)

#         cols = st.columns(5)

#         for i, row in enumerate(mood_movies.itertuples()):

#             movie_name = row.names

#             poster, rating = fetch_movie_data(movie_name)

#             trailer = fetch_trailer(movie_name)

#             with cols[i % 5]:

#                 if poster:
#                     st.image(poster, width=200)

#                 st.write(movie_name)

#                 if rating and rating != "N/A":
#                     st.write(f"⭐ {rating}")

#                 # ❤️ Favorite
#                 if st.button(
#                     "❤️ Favorite",
#                     key=f"mood_fav_{i}"
#                 ):

#                     add_favorite(
#                         st.session_state.username,
#                         movie_name,
#                         poster
#                     )

#                     st.success("Added to favorites")


#                 # ▶ Play Trailer
#                 if st.button(
#                     "▶ Play",
#                     key=f"mood_play_{i}"
#                 ):

#                     if trailer:

#                         st.session_state.trailer = trailer

#                         add_watch_history(
#                             st.session_state.username,
#                             movie_name,
#                             poster
#                         )

#                     else:

#                         st.warning(
#                             "Trailer not available"
#                         )

#             if (i + 1) % 5 == 0:
#                 cols = st.columns(5)

#     st.markdown("---")
    
#     # ==========================================
#     # 🔥 TRENDING MOVIES
#     # ==========================================

#     st.markdown("## 🔥 Trending Today")

#     trending_movies = fetch_trending_movies()

#     if trending_movies:

#         cols = st.columns(5)

#         for i, movie in enumerate(trending_movies):

#             with cols[i % 5]:

#                 if movie["poster"]:
#                     st.image(movie["poster"], width=200)

#                 st.write(movie["title"])

#                 st.write(f"⭐ {movie['rating']}")

#                 # ▶ Play Trailer
#                 if st.button("▶ Play", key=f"trend_{i}"):

#                     if movie["trailer"]:

#                         st.session_state.trailer = movie["trailer"]

#                     else:
#                         st.warning("Trailer not available")

#             if (i + 1) % 5 == 0:
#                 cols = st.columns(5)

#     else:

#         st.warning("Trending movies not loading")

   
    
    
#     # ==========================================
#     # FAVORITE MOVIES
#     # ==========================================

#     st.markdown("---")
#     st.markdown("## ❤️ My Favorite Movies")

#     favorites = get_favorites(
#     st.session_state.username
#     )

#     if favorites:

#         cols = st.columns(5)

#         for i, movie in enumerate(favorites):

#             with cols[i % 5]:
               
#                 if movie[1]:
#                     st.image(movie[1], width=200)

#                 st.write(movie[0])
#                 # ❌ Remove Button 
#                 if st.button( 
#                     "❌ Remove", key=f"remove_{i}" 
#                     ):
#                     remove_favorite(
#                          st.session_state.username,
#                            movie[0] 
#                            ) 
#                     st.rerun()
    

#             if (i + 1) % 5 == 0:
#                 cols = st.columns(5)

#     else:
#         st.info("No favorite movies yet")

#     # ==========================================
#     # WATCH HISTORY
#     # ==========================================

#     st.markdown("---")
#     st.markdown("## 📜 Recently Watched")

#     history = get_watch_history(
#         st.session_state.username
#     )

#     if history:

#         cols = st.columns(5)

#         for i, movie in enumerate(history[:10]):

#             with cols[i % 5]:

#                 if movie[1]:
#                     st.image(movie[1], width=200)

#                 st.write(movie[0])

#                 #❌ Remove Button 
#                 if st.button( 
#                     "❌ Remove", 
#                     key=f"history_remove_{i}" 
#                 ):
#                     remove_watch_history(
#                         st.session_state.username, 
#                         movie[0] 
#                     ) 
#                     st.rerun()

#             if (i + 1) % 5 == 0:
#                 cols = st.columns(5)

#     else:
#         st.info("No watch history yet")

#     # 🎭 Genre Rows
#     st.markdown("## 🎭 Browse by Genre")

#     def show_genre_row(genre_name):

#         st.markdown(f"### {genre_name}")

#         filtered = df[df['genre'].str.contains(genre_name, case=False, na=False)].head(10)

#         cols = st.columns(5)

#         for i, row in enumerate(filtered.itertuples()):

#             movie_name = row.names

#             poster, rating = fetch_movie_data(movie_name)
#             trailer = fetch_trailer(movie_name)

#             with cols[i % 5]:
                
#                 if poster:
#                     st.image(poster, width=200)

#                 st.write(movie_name)

#                 if rating and rating != "N/A":
#                     st.write(f"⭐ {rating}")

#                 if st.button("▶ Play", key=f"{genre_name}_{i}"):

#                     if trailer:
#                         st.session_state.trailer = trailer
#                     else:
#                         st.warning("Trailer not available")

#             if (i + 1) % 5 == 0:
#                 cols = st.columns(5)

#     # Call genre rows
#     show_genre_row("Action")
#     show_genre_row("Comedy")
#     show_genre_row("Drama")    
    

#     # 🎬 Video Player
#     if st.session_state.trailer:

#         st.markdown("## 🎬 Now Playing")
#         video_url = st.session_state.trailer

#         embed_url = video_url.replace(
#             "watch?v=",
#             "embed/"
#             )

#         st.video(embed_url)

#         if st.button("⛔ Stop", key="stop_video"):
#             st.session_state.trailer = None

# # else:

# #     st.title("🔐 Login Required")

# #     st.warning("Please login to access the app")





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