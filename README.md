# 🎬 Movie Recommendation System

An AI-powered Movie Recommendation Web Application built using **Python**, **Streamlit**, **Machine Learning**, and **TMDB API**.  
This project recommends movies similar to the selected movie and provides features like trailers, trending movies, favorites, watch history, mood-based recommendations, and smart search.

---

# 🚀 Features

## ✅ Movie Recommendation System
- Recommends similar movies using Machine Learning.
- Content-based filtering using NLP concepts.

---

## ✅ Smart Movie Search
- Search movies instantly.
- Intelligent search suggestions.

---

## ✅ Movie Posters & Ratings
- Fetches movie posters dynamically using TMDB API.
- Displays IMDb/TMDB ratings.

---

## ✅ Watch Movie Trailers
- Play movie trailers directly inside the app.
- Integrated YouTube trailer support.

---

## ✅ Trending Movies Section
- Displays daily trending movies using TMDB API.
- Includes posters, ratings, and trailer support.

---

## ✅ Mood-Based Recommendation
Users can choose mood-based categories:

- 😊 Happy → Comedy
- 😢 Emotional → Drama
- 😍 Romantic → Romance
- 😨 Thriller → Thriller
- 🤯 Mind-Bending → Sci-Fi
- 😎 Chill → Adventure

Movies are recommended according to the selected mood.

---

## ✅ Favorites Section
Users can:
- Add movies to favorites
- Remove movies from favorites

---

## ✅ Watch History
Users can:
- Save watched movies automatically
- Remove movies from recently watched section

---

## ✅ User Authentication
- Login System
- Registration System
- Logout Feature

---

## ✅ Responsive UI
- Supports both:
  - 🌙 Dark Mode
  - ☀️ Light Mode

---

## ✅ Premium Netflix-Style UI
- Hover animations
- Movie card effects
- Glassmorphism UI
- Gradient backgrounds
- Smooth transitions

---

# 🛠️ Technologies Used

## Frontend
- Streamlit
- HTML
- CSS

## Backend
- Python

## Machine Learning
- NLP
- Cosine Similarity
- CountVectorizer

## APIs
- TMDB API
- YouTube Trailer Support

## Database
- SQLite

---

# 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── main.py
├── auth.py
├── smart_search.py
├── movies.pkl
├── similarity.pkl
├── df.pkl
├── requirements.txt
├── README.md
└── users.db
```

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

---

## Step 2: Open Project Folder

```bash
cd movie-recommendation-system
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## Step 5: Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

---

# 🔑 TMDB API Setup

## Step 1:
Create account on:

```text
https://www.themoviedb.org/
```

---

## Step 2:
Generate API Key.

---

## Step 3:
Add API key inside `main.py`

Example:

```python
TMDB_API_KEY = "YOUR_API_KEY"
```

---

# 🧠 Machine Learning Concept Used

This project uses:

- Natural Language Processing (NLP)
- CountVectorizer
- Cosine Similarity

Movies are recommended based on:
- Genres
- Keywords
- Cast
- Crew
- Movie overview

---

# 🎨 UI Enhancements Added

## ✅ Hover Effects
Movie posters enlarge on hover.

---

## ✅ Glassmorphism Buttons
Modern transparent button design.

---

## ✅ Gradient Background
Netflix-inspired dark theme.

---

## ✅ Responsive Design
Supports light and dark system modes.

---

# 📸 Main Sections of App

## 🔐 Login / Register
User authentication system.

---

## 🎬 Hero Banner
Movie-themed welcome banner.

---

## 🔍 Smart Search
Search movies instantly.

---

## 🔥 Recommended Movies
AI-based recommendations.

---

## 😊 Mood Recommendation
Movies based on user mood.

---

## 🔥 Trending Today
Trending movies from TMDB.

---

## ❤️ Favorite Movies
User favorite collection.

---

## 📜 Recently Watched
Watch history section.

---

## 🎭 Browse by Genre
Action, Comedy, Drama, etc.

---

# 🧩 Future Improvements

- 🎤 Voice Search
- 🤖 AI Chatbot for movie suggestions
- 🌐 Multi-language support
- 📱 Mobile App
- ⭐ Personalized AI recommendations
- 🎵 Background music support

---

# 👨‍💻 Author

## Prerna Thakur

AI & Machine Learning Enthusiast

---

# 📜 License

This project is for educational purposes only.

---

# ⭐ Final Output

This project provides:

✅ AI-based movie recommendations  
✅ Trending movies  
✅ Mood-based recommendations  
✅ Trailer playback  
✅ Favorites system  
✅ Watch history  
✅ User authentication  
✅ Responsive Netflix-style UI  
✅ Streamlit web application  
✅ Machine Learning integration