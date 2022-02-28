import speech_recognition
from flask import Flask, render_template
from forms import DataForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "dick"


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

@app.route("/DataForm")
def DataForm():
    template = "DataForm.html"
    return render_template(template)

@app.route("/get-voice")
def get_voice():
    template= "DataForm.html"
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = recognizer.listen(source)
    userRequest = recognizer.recognize_google(audio)

    return render_template(template, response=userRequest)