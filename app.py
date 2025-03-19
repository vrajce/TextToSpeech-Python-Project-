from flask import Flask , render_template, request
import pyttsx3

app = Flask(__name__)

lastSpoken = []

def speakText(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@app.route('/' , methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        if text.lower() == "quit":
            speakText("GoodBye")
            return render_template('index.html' , message="GoodBye" , history=lastSpoken)
        speakText(text)
        lastSpoken.append(text)
        return render_template('index.html' , message="Spoken: " + text , histroy=lastSpoken)
    return render_template('index.html' , history=lastSpoken)

if __name__ == '__main__':
    app.run(debug=True)