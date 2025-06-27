"""Module providing a sentiment detector"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/")
def index():
    """Render template"""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    """Retrieve the text to analyze from the request"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    label = response['label']
    # Error Handling Function"""
    if len(label) == 0:
        return {'message':'Invalid text Please try again!'}
    score = response['score']
    # Return a formatted string with the sentiment label"""
    return {'label': label, 'score': score}

if __name__ == "__main__": # main function
    app.run(host="0.0.0.0", port=5000)
