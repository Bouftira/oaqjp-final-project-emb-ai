import requests
import json

def emotion_detector(text_to_analyse):
    # Define a function to return a dictionary with None for all values
    def get_empty_emotion_response():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # If the input text is blank, return None for all values
    if not text_to_analyse.strip():
        return get_empty_emotion_response()

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 200 and 'emotionPredictions' in formatted_response:
        emotion_data = formatted_response['emotionPredictions'][0].get('emotion', {})
        dominant_emotion = max(emotion_data, key=emotion_data.get, default=None)
        return {**emotion_data, "dominant_emotion": dominant_emotion}
    
    # If the status code is 400, return None for all values
    if response.status_code == 400:
        return get_empty_emotion_response()

    # Generic error handling for other unexpected responses
    return {"error": f"Request failed with status code {response.status_code}"}