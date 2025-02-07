from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import requests

app = Flask("emotionDetection")

@app.route("/")
def render_index_page():
    """index page """
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():

    text_to_analyze = request.args.get('textToAnalyze')

    
    emotions = emotion_detector(text_to_analyze)

    return f'''
    For the given statement, the system response is:
    'anger': {emotions.get('anger', 0)}, 
    'disgust': {emotions.get('disgust', 0)}, 
    'fear': {emotions.get('fear', 0)}, 
    'joy': {emotions.get('joy', 0)}, 
    'sadness': {emotions.get('sadness', 0)}. 
    The dominant emotion is {emotions.get('dominant_emotion', 'Not found')}.
    '''




if __name__ == "__main__":
    app.run(debug=True)