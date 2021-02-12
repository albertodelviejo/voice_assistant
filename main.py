import speech_recognition as sr

def audio_to_text():
    return obtain_audio()

def obtain_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    return recognize_speech_google(audio, r)

def recognize_speech_google(audio, r):
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = """credendiales de google"""
    try:
        text_detected = r.recognize_google(audio)
        print("Creo que has dicho " + text_detected) 
    except sr.UnknownValueError:
        print("No lo he entendido")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text_detected

audio_to_text()