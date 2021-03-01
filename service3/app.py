from flask import Flask, Response
import random

app = Flask(__name__)


@app.route('/volume', methods=['GET'])
def volume():
    volume = ['0.33', '0.5', '0.7']
    return Response(random.choices(volume), mimetype="text/plain")


if __name__=="__main__":
    app.run(port=5002, debug=True, host='0.0.0.0')