# # from gql import Client, gql
# # from gql.transport.aiohttp import AIOHTTPTransport
from playsound import playsound
# # # Select your transport with a defined url endpoint
# # transport = AIOHTTPTransport(url="http://localhost:8000/graphql")

# # # Create a GraphQL client using the defined transport
# # client = Client(transport=transport, fetch_schema_from_transport=True)

# # # transport = AIOHTTPTransport(url='YOUR_URL', headers={'Authorization': 'token'})

# # USERNAME="harman"
# # PASSWORD="123456"
# # # Provide a GraphQL query
# # query = gql(
# #     """
# #     mutation token ($uname: String!, $pass: String!) {
# #       tokenAuth (username: $uname, password: $pass) {
# #         token
# #       }
# #     }
# # """
# # )

# # params = {"uname": USERNAME,
# #     "pass":PASSWORD,
# # }

# # # Get name of continent with code "EU"
# # result = client.execute(query, variable_values=params)
# # print(result)


# import pyttsx3
# import speech_recognition as sr
# from google.cloud import speech_v1 as speech

# config = dict(language_code="pa-Guru-IN")
# r = sr.Recognizer()


# def speech_to_text(config, audio):
#     client = speech.SpeechClient()
#     response = client.recognize(config=config, audio=audio)
#     print_sentences(response)


# def print_sentences(response):
#     for result in response.results:
#         best_alternative = result.alternatives[0]
#         transcript = best_alternative.transcript
#         confidence = best_alternative.confidence
#         print("-" * 80)
#         print(f"Transcript: {transcript}")
#         print(f"Confidence: {confidence:.0%}")


# def SpeakText(command):

#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()
#     # engine.stop()


# while(1):

#     # Exception handling to handle
#     # exceptions at the runtime
#     try:

#         # use the microphone as source for input.
#         with sr.Microphone() as source2:

#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             # r.adjust_for_ambient_noise(source2, duration=0.3)
#             print("Continue")

#             # listens for the user's input
#             audio2 = r.listen(source2)

#             # Using google to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()

#             print("Did you say "+MyText)
#             SpeakText(MyText)

#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))

#     except sr.UnknownValueError:
#         print("unknown error occured")

file= 'response_file.mp3'
playsound(file)
