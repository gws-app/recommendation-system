# Activity Recommendation System (Dockerized)

This repository provides a **Dockerized Activity Recommendation System** that suggests activities based on user input using **TF-IDF vectorization** and **cosine similarity**.

## Features
- **Recommendation Engine**: Recommends activities based on text similarity.
- **Preprocessing**: Custom tokenization for flexible activity data handling.
- **Docker Deployment**: Easily deployable as a containerized service.

## Repository Structure
```
app
├── __pycache__
├── app.py
├── dataset.pkl
├── tfidf_matrix.pkl
├── utils.py
├── vectorizer.pkl
Dockerfile
LICENSE
requirements.txt
```

## Installation and Setup
```bash
pip install requirements.txt
```
### Prerequisites
Ensure you have Docker installed. You can download it from [Docker’s official website](https://www.docker.com/).

### Build the Docker Image
Run the following command to build the Docker image:
```bash
docker build -t activity-recommendation-app .
```

### Run the Docker Container
To start the application, use:
```bash
docker run -d -p 5000:5000 activity-recommendation-app
```
The application will be accessible at `http://localhost:5000`.

## Usage

### Endpoint: `/recommend`
Send a POST request with user input to receive activity recommendations.

#### Request Format
```json
{
  "activities": "walking | fasting | youtube"
}
```

#### Response Format
```json
{
  "recommended_activities": [
    "hiking",
    "meditation",
    "cycling"
  ]
}
```

### Example with `curl`
```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"activities": "walking | fasting | youtube"}' \
    http://localhost:5000/recommend
```

## Files and Artifacts
- **`app.py`**: Contains the Flask application logic for handling requests and serving recommendations.
- **`utils.py`**: Implements helper functions like custom tokenization and similarity calculation.
- **Pickle Files**:
  - `vectorizer.pkl`: Pretrained TF-IDF vectorizer.
  - `tfidf_matrix.pkl`: Precomputed TF-IDF matrix for activity data.
  - `dataset.pkl`: Serialized dataset used for recommendations.

## License
See the [LICENSE](https://github.com/gws-app/recommendation-system/blob/main/LICENSE) file for details.


## Acknowledgments
This recommendation system leverages:
- **Pandas** and **Scikit-learn** for data processing and machine learning.
- **Docker** for containerization and seamless deployment.
