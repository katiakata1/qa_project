from flask import Flask, render_template
import requests 

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    spirit = requests.get("http://localhost:5001/spirit")
    volume = requests.get("http://localhost:5002/volume")
    mixer = requests.post("http://localhost:5003/mixer", data = spirit)

    return render_template('index.html', spirit=spirit.text, volume = volume.text, mixer=mixer.text)

@app.route('/list', methods=['GET', 'POST'])
def list():
    return render_template('list.html')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')