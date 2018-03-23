from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Result
from helpers.classifierHelper import predict

app = Flask(__name__)

engine = create_engine('sqlite:///hr_sidekick.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# In case you get error (numpy.ndarray is not callable) , wrap the variable with str()
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login_post():
    user = request.form['text']
    processed_text = user.upper()
    #passwd = request.form['password']	
    return processed_text

@app.route('/rf_tester')
def input_data():
	return render_template('data_input.html')

@app.route('/rf_tester', methods=['POST'])
def generate_result():
    text = request.form['text']
    processed_text = [float(i) for i in text.split(',')]
    value = predict(processed_text, 'randomForest')
    if value[0] == 1:
        return render_template('result.html', cursor = 'Employee will not leave company.')
    else:
        return render_template('result.html', cursor = 'Employee will leave company.')
    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
app.run(host='0.0.0.0', port=5000)