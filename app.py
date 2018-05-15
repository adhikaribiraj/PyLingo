import time
import sys
import ServerSentEvent as sse
import SpeechToText as st
from googletrans import Translator
from flask import Flask
import flask as f
from flask import render_template, flash, session, Response
app = Flask(__name__)
app.secret_key = "super secret key"

# speechRecognizer = st.SpeechToText()
# listen = False
# text = None

@app.route("/")
def main():
    # text = speechRecognizer.listen()
    return render_template("index.html")

@app.route("/language/<language>")
def doTranslation(language):
    translator = Translator()
    line = file.readline()
    finalString = ""
    language = language.lower()
    while line:
        if language == "french":
            finalString += translator.translate(line, dest='fr').text
        elif language == "spanish":
            finalString += translator.translate(line, dest='es').text
        elif language == "english":
            finalString += translator.translate(line, dest='en').text
        line = file.readline()
    return finalString

@app.route("/chatData/<boolean>")
def sendChatData(boolean):
    def gen():
        try:
            speechRecog = st.SpeechToText()
            if boolean == "True":
                speechRecog.listen()
                text = speechRecog.getSentence()
                ev = sse.ServerSentEvent(text)
                yield ev.encode()
        except GeneratorExit:
            pass
    return Response(gen(), mimetype = "text/event-stream")


if __name__ == "__main__":
    app.run()
