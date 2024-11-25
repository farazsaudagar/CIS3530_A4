from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

from app import routes
from app import user_verification