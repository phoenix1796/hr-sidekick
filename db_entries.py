from argparse import ArgumentParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *

engine = create_engine('sqlite:///hr_sidekick.db', echo=True)
 
added_users = list()

def add_user(name, password):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = User(name, password)
    session.add(user)
    added_users.append(name)
    session.commit()

def remove_user(name):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(User).filter(User.name == name).delete()
    session.commit()
 
def accept_args():
    parse_args = ArgumentParser()
    parse_args.add_argument('--add', action = 'store_true')
    parse_args.add_argument('--remove', action = 'store_true')
    parse_args.add_argument('--user', action = 'store')
    parse_args.add_argument('--password', action = 'store')

def main():
    args = accept_args()
    session.commit()

