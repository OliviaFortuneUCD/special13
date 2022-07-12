from gtts import gTTS
import os






os.system("mpg321 hello.mp3")
tts = gTTS(text='Hello, World!', lang='en')
tts.save("hello.mp3")
os.system("mpg321 hello.mp3")