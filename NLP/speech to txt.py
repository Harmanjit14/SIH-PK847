import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
     print("Ask anything")
     audio=r.listen(source)
     print("Done")

result=r.recognize_google(audio,language="hi-IN")     
print(result)

print(r.recognize_google(audio,language="pa-Guru-IN"))
print(r.recognize_google(audio))
     