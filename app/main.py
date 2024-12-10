from flask import Flask, request, jsonify
from utils import custom_tokenizer
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import pandas as pd

app = Flask(__name__)

#load obj
with open('vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

with open('tfidf_matrix.pkl', 'rb') as tfidf_file:
    tfidf_matrix = pickle.load(tfidf_file)

with open('dataset.pkl', 'rb') as dataset_file:
    df = pickle.load(dataset_file)

# recomm
def recommend_activities(input_activities, df, vectorizer, tfidf_matrix, top_n=5):
    input_vector = vectorizer.transform([input_activities])
    input_cosine_sim = cosine_similarity(input_vector, tfidf_matrix)

    sim_scores = list(enumerate(input_cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]
    activity_indices = [i[0] for i in sim_scores]

    similar_activities_df = df.iloc[activity_indices][['activities']].copy()
    similar_activities_df['activities_list'] = similar_activities_df['activities'].apply(
        lambda x: [activity.strip() for activity in x.split('|')]
    )

    all_activities = [activity for sublist in similar_activities_df['activities_list'] for activity in sublist]
    input_activities_list = [activity.strip() for activity in input_activities.split('|')]
    filtered_activities = [activity for activity in all_activities if activity not in input_activities_list]

    activity_counts = Counter(filtered_activities)
    sorted_activities = sorted(activity_counts.keys(), key=lambda x: activity_counts[x], reverse=True)

    return sorted_activities

# endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    input_data = request.json
    input_activities = input_data.get('activities', '')
    if not input_activities:
        return jsonify({'error': 'Activities input is required'}), 400

    recommendations = recommend_activities(input_activities, df, vectorizer, tfidf_matrix)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)