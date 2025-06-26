from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion__detector

app = Flask("Sentiment Analyzer")

@app.route("/")
def index():

    # Render template 
    return render_template("index.html")

# Sentiment Analyzer
@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

     # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Return a formatted string with the sentiment label and score
    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)