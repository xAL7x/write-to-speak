# pip install gtts 
print("-------created by alhassan alharbi -------")
from gtts import gTTS
import os
tts=gTTS(input("enter the text : "),lang=input("enter the languge --> "))
a=input('enter the file name 》》》')
tts.save(a+'.mp3')
os.system(a+".mp3")

