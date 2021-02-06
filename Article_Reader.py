import envs.pytorchenv.Lib.encodings.shift_jisx0213import requests
from bs4 import BeautifulSoup
url = str(input("Paste article url\n"))

def content(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles=[]
    for i in range(len(soup.select('.p'))):
        article = soup.select('.p')[i].getText().strip()
        articles.append(article)
        contents =" ".join(articles)
    return contents

engine = tyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty(voice , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
contents = content(url)
print(contents)