from curses import nl
from uuid import uuid4
from google.cloud import texttospeech
import random
import json
import time
import torch
from model import NeuralNet
from utils import bag_of_words, case_selector, token
import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"key.json"


language = 'pa-IN'
recognize_language = 'en-US'

# Load NLP Model Files
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'rb') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Friday Night SIH"

client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(
    language_code="pa-IN", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)

r = sr.Recognizer()
keyword = "hazel"


def nlp(text):
    sentence = token(text)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:

            if tag == intent["tag"]:
                response = intent['responses']
                resp = random.choice(response)
                if not isinstance(resp, int):
                    pass
                else:
                    print(response[0])
                    case_selector(int(response[0]))
    else:
        print(f"{bot_name}: I do not understand...")


with sr.Microphone() as source:
    print('Adjusting mic')
    r.adjust_for_ambient_noise(source=source, duration=5)
while True:

    with sr.Microphone() as source:
        print("Listening to Hazel")
        audio = r.listen(source, timeout=1, phrase_time_limit=2)
    try:
        text = r.recognize_google(audio, language=recognize_language)
        print(text)
        if text == 'Hazel' or text == 'hazel':

            with sr.Microphone() as source2:
                print("Listening to Query")
                query = r.listen(source2, timeout=3, phrase_time_limit=5)
            try:
                text2 = r.recognize_google(query, language=language)
                # text2 = r.recognize_google_cloud(query, language=language, credentials_json=None)
                print(text2)
                text2 = nlp(text)
                synthesis_input = texttospeech.SynthesisInput(text=text2)
                response_voice = client.synthesize_speech(
                    input=synthesis_input, voice=voice, audio_config=audio_config)
                file = f'{uuid4()}.mp3'
                with open(file, "wb") as out:
                    out.write(response_voice.audio_content)
                playsound(file)
                time.sleep(0.5)
                os.remove(file)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

time.sleep(0.1)
