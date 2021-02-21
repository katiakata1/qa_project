from flask import Flask, render_template
import requests 

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    #Gets an animal
    animal = requests.get('http://localhost:5001/animal')
    #Gets the noise 
    noise = requests.post('http://localhost:5001/noise', data=animal.text)

    return render_template('index.html', animal=animal.text, noise=noise.text)


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')