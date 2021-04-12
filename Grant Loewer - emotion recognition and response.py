#Grant Loewer - KSU COMP730 FALL2020 - Final Project
#README located within the same directory.

#USED
#https://github.com/Uberi/speech_recognition/blob/master/examples/background_listening.py
#https://realpython.com/playing-and-recording-sound-python/#recording-audio
#https://sonsuzdesign.blog/2020/05/22/convert-your-speech-to-text-using-python/

#UNUSED
#https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
#https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
#https://www.codespeedy.com/print-mic-name-device-id-in-python/

#*****speech recognition*****
import speech_recognition
import pyaudio
import time

#record audio and save to file
def callback(recognizer, audio):
    try:
        result = recognizer.recognize_google(audio)
        print(result)
    except speech_recognition.UnknownValueError:
        print("I didn't get that")
    except speech_recognition.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

recognizer = speech_recognition.Recognizer()
print(speech_recognition.Microphone.list_microphone_names())

microphone = speech_recognition.Microphone(device_index=2)

with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    
print("Listening")

recognizer.listen_in_background(microphone, callback)
stop_listening = recognizer.listen_in_background(microphone, callback)

print("Not Listening")
