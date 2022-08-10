import random
import json
import time
import torch
from model import NeuralNet
from utils import bag_of_words, case_selector, token
from google.cloud import texttospeech
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"key.json"


speech_client = texttospeech.TextToSpeechClient()
# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="pa-IN", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)


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
print("Let's chat! (type 'quit' to exit)")


while True:

    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = token(sentence)
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

                    print(f"{bot_name}: {resp}")

                    synthesis_input = texttospeech.SynthesisInput(
                        text=resp)

                    response_voice = speech_client.synthesize_speech(
                        input=synthesis_input, voice=voice, audio_config=audio_config)

                    with open("output.mp3", "wb") as out:
                        out.write(response_voice.audio_content)
                        os.startfile('output.mp3')
                else:
                    print(response[0])
                    case_selector(int(response[0]))
    else:
        print(f"{bot_name}: I do not understand...")

time.sleep(0.1)
