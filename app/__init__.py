import os

from flask import Flask

from flask_login import LoginManager
from config import basedir, FIREBASE_CONFIG

import pyrebase
from firebase_admin import credentials

app = Flask(__name__)
app.config.from_object('config')

#lm = LoginManager()
#lm.init_app(app)
#lm.login_view="account"

#firebase = firebase.FirebaseApplication('https://final-33b0a.firebaseio.com/',None)
cred = credentials.Certificate('/home/ubuntu/551final/app/final_33b0a_firebase_adminsdk_vjuqw_d474b38d4b.json')
fbapp = pyrebase.initialize_app(FIREBASE_CONFIG)
auth = fbapp.auth()
db = fbapp.database()
storage = fbapp.storage()

from app import views
#from app import models

