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
def fooBar():
    a = predict([0.38,0.53,2,157,3,0,0,1],"randomForest")
    return str(a) # sample sending the prediction directly to frontend

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
app.run(host='0.0.0.0', port=5000)