from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/spirit', methods=['GET'])
def spirit():
    spirit = ['Vodka', 'Gin', 'Rum', 'Jagermeister']
    return Response(random.choices(spirit), mimetype="text/plain")



if __name__=="__main__":
    app.run(port=5001, debug=True, host='0.0.0.0')