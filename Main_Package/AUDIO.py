from .READ import language_abreviation as la
from .READ import language
import os
import random

from gtts import gTTS
import playsound
import speech_recognition as sr


def speak(text):
    r = random.randint(1,1000)
    tts = gTTS(text=text, lang= f'{la()}')
    audio_file = f"{language()} "+str(r)+".mp3"
    tts.save(audio_file)
    print('\n'+ ' ' + text)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def get_audio(lg="language 2.txt"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\n listening...')
        audio = r.listen(source)
        voice_data=""

        try:
            f = open("name of owner.txt", "rt")
            Name = f.read()
            voice_data = r.recognize_google(audio, language = f"{la(lg)}") # type: ignore
            print(f"\n {Name}: {voice_data}")

        except Exception as e:
            print("\n I am sorry, I could not understand, please repete... "+ str(e))

    return voice_data.lower()
