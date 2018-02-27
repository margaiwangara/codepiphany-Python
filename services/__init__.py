from flask import Flask

app = Flask(__name__)

from services.auth.testroute import mod
from services.auth.routes import mod
from services.auth.loginroute import mod

app.register_blueprint(auth.testroute.mod)
app.register_blueprint(auth.routes.mod,url_prefix="/users")
app.register_blueprint(auth.loginroute.mod,url_prefix="/users")

#secret key
app.secret_key = "InanaSarkis"