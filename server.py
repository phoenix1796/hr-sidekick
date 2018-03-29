from flask import Flask, render_template, url_for, request, redirect, flash, jsonify, session, abort
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Result
from helpers.classifierHelper import predict
import helpers.visualizer as vis
from helpers.classifierHelper import _loadClassifier

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

engine = create_engine('sqlite:///hr_sidekick.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)



#################


@app.route('/rf_tester')
def input_data():
    error = None
    if not session.get('logged_in'):
        error = 'You need to login first.'
        return render_template('login.html', error=error)
    else:
        return render_template('data_input.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.name.in_(
            [POST_USERNAME]), User.password.in_(
            [POST_PASSWORD]))
        result = query.first()
        if result:
            session['logged_in'] = True
            return redirect(url_for('input_data'))
        else:
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return login()


############


''' 
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('input_data'))
    return render_template('login.html', error=error)    
    
@app.route('/rf_tester')
def input_data():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
    	return render_template('data_input.html')'''


@app.route('/rf_tester', methods=['POST'])
def generate_result():
    text = request.form['text']
    processed_text = [float(i) for i in text.split(',')]
    value = predict(processed_text, 'randomForest')
    vis.input_data_chart(processed_text)
    clf = _loadClassifier("classifiers/randomForest.pkl")  # % classifierName)
    vis.feature_importances(clf)
    if value[0] == 1:
        return render_template('result.html', cursor='Employee will not leave company.')
    else:
        return render_template('result.html', cursor='Employee will leave company.')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
app.run(host='0.0.0.0', port=5000)
