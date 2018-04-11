from argparse import ArgumentParser
from sqlalchemy.orm import sessionmaker
from database_setup import *

engine = create_engine('sqlite:///hr_sidekick.db', echo=True)


def add_user(name, password):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = User(name, password)
    session.add(user)
    session.commit()


def remove_user(name):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(User).filter(User.name == name).delete()
    session.commit()


def accept_args():
    args = ArgumentParser()
    group = args.add_mutually_exclusive_group()
    group.add_argument('--add', action='store_true')
    group.add_argument('--remove', action='store_true')
    args.add_argument('--user', action='store')
    args.add_argument('--passwd', action='store')
    return args.parse_args()


def main():
    args = accept_args()
    if args.add:
        add_user(args.user, args.passwd)
    elif args.remove:
        remove_user(args.user)


if __name__ == '__main__':
    main()
