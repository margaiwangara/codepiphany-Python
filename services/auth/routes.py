from flask import Blueprint,render_template,request,flash,logging,url_for
from acquire.functions.routes import username_validation,validate_email,password_match
from acquire.models import Users
from acquire import db
from passlib.hash import sha256_crypt
from flask import current_app

mod = Blueprint('auth',__name__,template_folder="templates")

@mod.route("/auth/register",methods=["POST","GET"])
def user_registration():
    #check method of execution
    if request.method == "POST":
        #log occurence
        current_app.logger.info("Form Submitted: Method = POST")

        #check to see if input is empty then validate with functions
        if request.form['signup_username'] is not None:
            username = username_validation(request.form['signup_username'])
        if request.form['signup_email'] is not None:
            email = validate_email(request.form['signup_email'])
        if request.form['signup_password'] is not None:
            password = password_match(request.form['signup_password'],request.form['signup_cpassword'])
        
        if password != 1 and email != 1 and username != 1:
            #write a log
            print("All inputs have been verified and cleared")

            #encrypt password
            hashed_password = sha256_crypt.encrypt(str(password))

            user = Users.query.filter((Users.email == email) | (Users.username == username)).first()
            if user is None:
                #insert if data not found
                user_insert = Users(email=email, password=hashed_password, username=username, tandcs='1')
                #add to db
                db.session.add(user_insert)
                #commit
                db.session.commit()

                #success message
                msg = "Registration Successful. Please check your email to activate your account"
                return render_template("signup.html",msg=msg)
            else:
                error = "Username or email already exist. Please try again"
                return render_template("signup.html",error=error)
        else:
            error = "Invalid or null data input"    
            return render_template("signup.html",error=error)
    return render_template("signup.html")
