from flask import Flask, Response
import random

app = Flask(__name__)


@app.route('/volume', methods=['GET'])
def volume():
    volume = ['1/3 ', '1/2 ', '7/10 ']
    return Response(random.choices(volume), mimetype="text/plain")


if __name__=="__main__":
    app.run(port=5002, debug=True, host='0.0.0.0')