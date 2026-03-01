"""
This module implements a Flask server for an Emotion Detection application.
It provides endpoints to render the web interface and to process text
to identify emotions such as anger, disgust, fear, joy, and sadness.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyzes the sentiment of the provided text and returns a formatted string.
    If the input is invalid or blank, it returns an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and receive the response
    response = emotion_detector(text_to_analyze)

    # Extract dominant_emotion and handle the None case
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Format the response string as per the customer's requirement
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index.html page for the user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost port 5000
    app.run(host="0.0.0.0", port=5000)
    