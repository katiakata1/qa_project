from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.233.220.25/lists'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Lists(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spirit = db.Column(db.String(30), nullable=False)
    volume = db.Column(db.String(30), nullable=False)
    mixer = db.Column(db.String(5000), nullable=False)


@app.route('/', methods=['GET'])
def index():
    spirit = requests.get("http://service2:5001/spirit")
    volume = requests.get("http://service3:5002/volume")
    mixer = requests.post("http://service4:5003/mixer", data = spirit)

    db_data = Lists(spirit=spirit.text, volume = volume.text, mixer=mixer.text)
    db.session.add(db_data)
    db.session.commit()

    return render_template('index.html', spirit=spirit.text, volume = volume.text, mixer=mixer.text)


@app.route('/list', methods=['GET', 'POST'])
def list():
    spiritData = Lists.query.order_by(Lists.id.desc()).limit(5)
    return render_template('list.html', lists=spiritData)
######

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')