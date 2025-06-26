from flask import Flask, render_template

app = Flask(__name__)

#Read Operation basic route 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("\emotionDetector")
def emotion__detector(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # Return the response text from the API
    return response.text  
    

# Run the Application
if __name__ =="__main__":
    app.run(debug=True)