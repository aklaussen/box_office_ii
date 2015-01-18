from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': "box_office_db"}
app.config['SECRET_KEY'] = "KissAndTell"
app.config['SERVE_NAME'] = '127.0.0.1:1428'

db = MongoEngine(app)

def register_blueprints(app):
    from box_office_ii.views import movies
    from box_office_ii.admin import admin
    app.register_blueprint(movies)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run(port=1428)
