import json
from os.path import join, dirname
import os
from watson_developer_cloud import SpeechToTextV1

def speechaf(name):
    url = "https://stream.watsonplatform.net/speech-to-text/api"
    username = "21aab91c-292c-4d2a-9241-d98120cadd6b"
    password = "QpuVjyRqCuyp"

    filepath = os.getcwd() + "/trump_speech_files/" + name

    audio = open(filepath, 'rb')

    speech_to_text = SpeechToTextV1(
        username=username,
        password=password,
        x_watson_learning_opt_out=False
    )

    a = json.dumps(
        speech_to_text.recognize(audio, continuous=True, content_type="audio/wav", timestamps=True, word_confidence=True,
                                 word_alternatives_threshold=1), indent=2)
    b = json.loads(a)

    array=[];

    for i in range(len(b["results"])):
        for j in range(len(b["results"][i]["alternatives"][0]["timestamps"])):
            word = (b["results"][i]["alternatives"][0]["timestamps"][j][0])  # word
            start = (b["results"][i]["alternatives"][0]["timestamps"][j][1])  # start
            end = (b["results"][i]["alternatives"][0]["timestamps"][j][2])  # end
            confidence = (b["results"][i]["alternatives"][0]["word_confidence"][j][1])  # confidence

            array.append([word, start, end, confidence])

    return array

