import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Sample dataset: Users and their ratings for movies
data = {
    'User': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
    'Inception': [5, 4, 3, 0, 2],
    'The Matrix': [4, 0, 5, 3, 2],
    'Interstellar': [0, 2, 4, 4, 5],
    'The Dark Knight': [3, 3, 0, 2, 4],
    'Shawshank Redemption': [5, 0, 3, 0, 1],
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Set the 'User' column as the index
df.set_index('User', inplace=True)

print("User-Item Matrix (Movies and Ratings):")
print(df)

# Step 1: Calculate Cosine Similarity between users
similarity_matrix = cosine_similarity(df)

# Create a DataFrame from the similarity matrix for better readability
similarity_df = pd.DataFrame(similarity_matrix, index=df.index, columns=df.index)

print("\nUser Similarity Matrix (Cosine Similarity):")
print(similarity_df)

# Step 2: Recommend movies to a specific user based on similar users
def get_recommendations(user, df, similarity_df, top_n=2):
    if user not in df.index:
        print(f"User '{user}' not found in the dataset.")
        return []
    
    # Get the user's movie ratings
    user_ratings = df.loc[user]
    
    # Find users with similar tastes (sorted by similarity score)
    similar_users = similarity_df[user].sort_values(ascending=False)
    
    recommendations = {}

    # For each similar user
    for similar_user, similarity_score in similar_users.items():
        if similar_user == user:
            continue  # Skip the current user
        
        # Get the movies the similar user liked (rated > 0) but the current user hasn't rated yet
        similar_user_ratings = df.loc[similar_user]
        unrated_movies = user_ratings[user_ratings == 0].index
        
        for movie in unrated_movies:
            if similar_user_ratings[movie] > 0:  # Only consider movies the similar user liked
                if movie not in recommendations:
                    recommendations[movie] = 0
                # Weight the recommendation by similarity score
                recommendations[movie] += similar_user_ratings[movie] * similarity_score

    # Sort recommendations by the highest scores
    recommended_movies = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    if len(recommended_movies) == 0:
        print(f"No recommendations available for {user}. They might have already rated all movies.")
    
    # Return the top N recommendations
    return recommended_movies[:top_n]

# Take input for the user
user = input("Enter the user's name (e.g., Alice, Bob, Carol, Dave, Eve): ")

# Get the recommendations for the input user
print(f"\nTop movie recommendations for {user}:")
recommendations = get_recommendations(user, df, similarity_df, top_n=2)

if recommendations:
    for movie, score in recommendations:
        print(f"{movie} (score: {score:.2f})")
