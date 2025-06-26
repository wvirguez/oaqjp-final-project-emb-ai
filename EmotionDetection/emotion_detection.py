import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    anger_score = formatted_response['documentSentiment']['score']
    disgust_score = formatted_response['documentSentiment']['score']
    fear_score = formatted_response['documentSentiment']['score']
    joy_score = formatted_response['documentSentiment']['score']
    sadness_score = formatted_response['documentSentiment']['score']
    dominant_emotion = max(formatted_response['documentSentiment']['score']) 
    # Returning a dictionary containing sentiment analysis results
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score,'dominant_emotion': '<name of the dominant emotion>'
}  