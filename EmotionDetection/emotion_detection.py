import requests
import json



def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header )

    formatted_response = json.loads(response.text)

    emotion_data = formatted_response['emotionPredictions'][0]['emotion']




    results = {}
    for emotion, score in emotion_data.items():
        results[emotion] = score

    dominant_emotion = max(results, key=results.get)
    results["dominant_emotion"] = dominant_emotion


    return results
#results  = emotion_detector("I am so happy I am doing this")
#print(results)