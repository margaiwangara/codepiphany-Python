from acquire.models import Users
from acquire import db
from flask import Blueprint

mod = Blueprint('testroute',__name__)

@mod.route("/test",methods=["GET","POST"])
def testdb():
   user_input = Users(email="me@test.com", username="me", password="mypassword", tandcs="1")
   db.session.add(user_input)
   db.session.commit()

   return "Database input working"
