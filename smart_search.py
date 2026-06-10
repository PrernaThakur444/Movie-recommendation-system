from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle

# Load dataset
df = pickle.load(open("df.pkl", "rb"))

# Load NLP model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create combined text
df['combined'] = (
    df['names'].fillna('') + " " +
    df['genre'].fillna('')
)

# Create embeddings
movie_embeddings = model.encode(
    df['combined'].tolist(),
    show_progress_bar=True
)


# SMART SEARCH FUNCTION
def smart_search(query, top_n=5):

    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        movie_embeddings
    )[0]

    top_indices = similarities.argsort()[-top_n:][::-1]

    results = df.iloc[top_indices]['names'].tolist()

    return results