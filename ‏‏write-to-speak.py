# pip install gtts 
print("-------created by alhassan alharbi -------")
from gtts import gTTS
import os
tts=gTTS('my name is hassan ',lang='en')
tts.save('hassan.mp3')
os.system("hassan.mp3")