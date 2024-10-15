# 🎃 Movie Recommendation System 🎬 (Halloween Themed)
Welcome to the Movie Recommendation System! This is a *Flask-based web application* that allows users to get personalized movie recommendations based on a variety of inputs. The user can type in a movie title, select a language, or choose a genre from the dropdown list to receive movie suggestions. In the spirit of the season, the website features a spooky Halloween theme, complete with dark colors, eerie fonts, and spider webs for a festive touch!

## 🌟 Features
- Movie Recommendations by Title: Users can type in the title of a movie to receive recommendations based on that title.
- Recommendations by Language: Users can select a language from a dropdown menu and get movie recommendations in that language.
- Recommendations by Genre: Users can choose a movie genre to receive genre-based movie suggestions.
- Randomized Recommendations: If the user clicks the "Get Recommendations" button again, the system fetches a different set of movies with no repetition.
- Reset Functionality: There is a reset button to clear all fields and return the user to the main page.
- Halloween-Themed Design: A dark, spooky theme with spider webs and other Halloween elements adds an eerie, festive touch to the app.
- Pagination for Results: Recommendations are displayed in sets of 10, with no more than 10 results at a time.

## 💡 Usage
- Enter a Movie Title: In the search bar, type a movie title and click "Get Recommendations" to receive a list of 10 similar movies.
- Select a Language: Choose a language from the dropdown list, and the system will recommend 10 movies in that language.
- Select a Genre: Choose a genre from the dropdown list to get genre-based movie recommendations.
- Hit Reset: Clear all the fields and go back to the homepage by clicking the "Reset" button.

## ⚙️ How It Works
- Dataset: The recommendation system uses the TMDB top-rated movies dataset with over 9,000 movies. This dataset includes details such as movie titles, genres, language, and ratings.
- Core Algorithm: The system uses TF-IDF Vectorization to convert the movie genres into vectors, and cosine similarity to calculate the similarity between movies.
For title-based recommendations, the app finds the most similar movies to the user’s input using the cosine similarity score.
For language- and genre-based recommendations, movies are filtered from the dataset according to the user’s selection.
- Recommendations: If a movie title is provided, the system calculates the top 10 similar movies.
If a language or genre is selected, the system randomly picks 10 movies that match the selected parameter.
The system prevents repeating the same movies if the "Get Recommendations" button is clicked multiple times.

## 🛠️ Technologies Used
- Python: Main programming language used for backend logic.
- Flask: Python web framework to build the app and handle routes.
- Pandas: Used to handle and process the movie dataset.
- Scikit-learn: For the TF-IDF vectorization and cosine similarity computation.
- HTML/CSS: Frontend structure and Halloween-themed design.
- JavaScript: For additional UI interactions.
- FontAwesome: For adding spooky icons to enhance the Halloween theme.

## 🎯 Future Improvements
- User Ratings: Allow users to rate the recommendations and improve results using collaborative filtering.
- Movie Trailers: Provide links to movie trailers.
- Authentication: Add user login/signup for personalized recommendations.
- More Genres/Languages: Expand the available genres and languages in the dropdown lists.
- Recommendation History: Display the user’s previous recommendations.

