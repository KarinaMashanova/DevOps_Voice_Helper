import speech_recognition
from flask import Flask, render_template, request
from forms import DataForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "dick"


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


if __name__ == '__main__':
    app.run(debug=True)




