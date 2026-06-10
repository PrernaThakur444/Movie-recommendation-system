import sqlite3
import bcrypt

# Connect database
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()


# Register User
def register_user(username, password):

    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        conn.commit()
        return True

    except:
        return False


# Login User
def login_user(username, password):

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    data = cursor.fetchone()

    if data:

        stored_password = data[0]

        if bcrypt.checkpw(
            password.encode('utf-8'),
            stored_password
        ):
            return True

    return False

# ==========================================
# FAVORITES TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    movie_name TEXT,
    poster TEXT
)
""")


# ==========================================
# WATCH HISTORY TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS watch_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    movie_name TEXT,
    poster TEXT
)
""")

conn.commit()


# ==========================================
# ADD FAVORITE MOVIE
# ==========================================

def add_favorite(username, movie_name, poster):

    cursor.execute(
        """
        INSERT INTO favorites
        (username, movie_name, poster)
        VALUES (?, ?, ?)
        """,
        (username, movie_name, poster)
    )

    conn.commit()


# ==========================================
# GET FAVORITE MOVIES
# ==========================================

def get_favorites(username):

    cursor.execute(
        """
        SELECT movie_name, poster
        FROM favorites
        WHERE username=?
        """,
        (username,)
    )

    return cursor.fetchall()


# ==========================================
# ADD WATCH HISTORY
# ==========================================

def add_watch_history(username, movie_name, poster):

    cursor.execute(
        """
        INSERT INTO watch_history
        (username, movie_name, poster)
        VALUES (?, ?, ?)
        """,
        (username, movie_name, poster)
    )

    conn.commit()


# ==========================================
# GET WATCH HISTORY
# ==========================================

def get_watch_history(username):

    cursor.execute(
        """
        SELECT movie_name, poster
        FROM watch_history
        WHERE username=?
        ORDER BY id DESC
        """,
        (username,)
    )

    return cursor.fetchall()

# ❌ Remove Favorite Movie
def remove_favorite(username, movie_name):

    cursor.execute(
        """
        DELETE FROM favorites
        WHERE username=? AND movie_name=?
        """,
        (username, movie_name)
    )

    conn.commit()


# ❌ Remove Watch History
def remove_watch_history(username, movie_name):

    cursor.execute(
        """
        DELETE FROM watch_history
        WHERE username=? AND movie_name=?
        """,
        (username, movie_name)
    )

    conn.commit()


