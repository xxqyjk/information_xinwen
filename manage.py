from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis


class Config(object):
    DEBUG = True

    

    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information_xinwen'


app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()

