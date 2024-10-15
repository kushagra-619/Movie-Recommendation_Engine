from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import random

app = Flask(__name__)

# Load your movie dataset
movies_df = pd.read_csv("")  # Update this path

# Define the TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['Genres'].astype(str))

# Calculate the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Dictionary to store previously recommended indices for each user session
previous_recommendations = {}

def get_recommendations(title=None, language=None, genre=None, session_id=None, request_count=0):
    global previous_recommendations
    if session_id not in previous_recommendations:
        previous_recommendations[session_id] = {'indices': set(), 'request_count': 0}  # Initialize with an empty set and request count

    recommendations = pd.DataFrame()

    if title:
        idx = movies_df.index[movies_df['title'] == title].tolist()
        if idx:
            idx = idx[0]
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            movie_indices = [i[0] for i in sim_scores[1:]]  # Get all recommendations

            # Shuffle and pick top 10 recommendations
            random.shuffle(movie_indices)
            movie_indices = movie_indices[:10]
            recommendations = movies_df.iloc[movie_indices][['title', 'vote_average', 'original_language']]


            # Exclude previously recommended movies
            movie_indices = [i for i in movie_indices if i not in previous_recommendations[session_id]['indices']]
            recommendations = movies_df.iloc[movie_indices][['title', 'vote_average', 'original_language']]

    if language:
        lang_recommendations = movies_df[movies_df['original_language'] == language].sample(frac=1).head(10)
        lang_indices = lang_recommendations.index.tolist()

        # Exclude previously recommended movies
        lang_indices = [i for i in lang_indices if i not in previous_recommendations[session_id]['indices']]
        recommendations = pd.concat([recommendations, lang_recommendations.loc[lang_indices][['title', 'vote_average', 'original_language']]])

    if genre:
        genre_recommendations = movies_df[movies_df['Genres'].str.contains(genre, na=False)].sample(frac=1).head(10)
        genre_indices = genre_recommendations.index.tolist()

        # Exclude previously recommended movies
        genre_indices = [i for i in genre_indices if i not in previous_recommendations[session_id]['indices']]
        recommendations = pd.concat([recommendations, genre_recommendations.loc[genre_indices][['title', 'vote_average', 'original_language']]])

    # Remove duplicates and limit to 10 total recommendations
    recommendations = recommendations.drop_duplicates().reset_index(drop=True)
    recommendations = recommendations.head(10)  # Limit to 10 recommendations

    # Add newly recommended movies to the previous recommendations set
    for index in recommendations.index:
        previous_recommendations[session_id]['indices'].add(index)

    # Track how many times recommendations have been requested
    previous_recommendations[session_id]['request_count'] += 1

    # If there are not enough recommendations available, just return what is available
    if len(previous_recommendations[session_id]['indices']) >= len(movies_df):
        return pd.DataFrame(columns=['title', 'vote_average', 'original_language'])  # Return empty if all movies are shown

    return recommendations

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the selected movie, language, or genre
        selected_movie = request.form.get('movie')
        selected_language = request.form.get('language')
        selected_genre = request.form.get('genre')

        # Use session ID to track recommendations
        session_id = request.cookies.get('session_id', None)

        if not session_id:
            session_id = str(hash(request.remote_addr))  # Simple session ID based on IP address
            # Set a cookie to keep track of session_id (optional)
            resp = app.make_response(render_template('index.html', recommendations=None))
            resp.set_cookie('session_id', session_id)
            return resp

        recommendations = get_recommendations(selected_movie, selected_language, selected_genre, session_id)

        return render_template('index.html', recommendations=recommendations)

    return render_template('index.html', recommendations=None)

if __name__ == '__main__':
    app.run(debug=True)
