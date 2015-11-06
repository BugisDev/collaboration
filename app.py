from flask import Flask, render_template
from db import database
from models import tim3

app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)

@app.route("/") 
def home():
	collaboration = tim3.query.filter_by(id=1).first()
	print(dir (collaboration))
	return render_template('index.html', **locals()) 

if __name__ == "__main__":
	app.run()




