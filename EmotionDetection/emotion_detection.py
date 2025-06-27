import requests  # Import the requests library to handle HTTP requests
import json


# Watson NLP  pre-trained models
# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyze):  
    if len(text_to_analyze) == 0:
        return {'label': "Invalid text! Please try again!", 'score': "None"}
    else:
        url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
        myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
        header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
        response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        # Extracting sentiment label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score} 
  