from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
trans = gTTS(text = 'hello this is tom', lang = language, slow = False)

trans.save(audio)
playsound(audio)


# Alternative
# from gtts import gTTS
# tts = gTTS('hello')
# tts.save('hello.mp3')
