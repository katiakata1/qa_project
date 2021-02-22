from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/mixer', methods=['POST'])
def mixer():
    spirit = request.data.decode('utf-8')
    if spirit == 'Vodka':
        mixers = ['Orange Juice', 'Cranberry Juice', 'Tomato Juice', 'Soda Water', 'Tonic Water', 'Coke']
        mixer = random.choices(mixers)
        return Response(mixer, mimetype="text/plain")

    elif spirit == 'Gin':
        mixers = ['Vermouth', 'Tonic', 'Pineapple Juice', 'Flavored Schweppes']
        mixer = random.choices(mixers)
        return Response(mixer, mimetype="text/plain")

    elif spirit == 'Rum':
        mixers = ['Tonic Water', 'Coke', 'Ginger Beer', 'Flavored Seltzer']
        mixer = random.choices(mixers)
        return Response(mixer, mimetype="text/plain")

    else:
        mixers = ['Red Bull', 'Coke', 'Orange juice', 'Ginger ale', 'Ginger beer']
        mixer = random.choices(mixers)
        return Response(mixer, mimetype="text/plain")



if __name__=="__main__":
    app.run(port=5003, debug=True, host='0.0.0.0')