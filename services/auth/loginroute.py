from flask import Blueprint,render_template,logging,session,flash,url_for,redirect,request
from acquire.functions.routes import password_validate,username_validation
from acquire.models import Users
from acquire import db
from passlib.hash import sha256_crypt
from flask import current_app

mod = Blueprint("user_login",__name__,template_folder='templates',static_folder='static')

@mod.route("/auth/access",methods=["GET","POST"])
def account_access():
    if request.method == "POST":
        #log form submition
        current_app.logger.info("Login Form Submitted: Method = POST")

        #get from data and validate
        if request.form['login_password'] is not None:
            username = username_validation(request.form['login_username'])
        if request.form['login_password'] is not None:
            password = password_validate(request.form['login_password'])

        #check if result != 1 and continue
        if password is not 1 and username is not 1:
            #log input pass
            current_app.logger.info("Input validation passed")

            #get user data and check db
            login_query = Users.query.filter(Users.username == username).first()

            if login_query is not None:
                #check password
                new_password = login_query.password

                if sha256_crypt.verify(password,new_password):
                    #log password verification pass
                    current_app.logger.info("Password matches")
                    #set session
                    #secret key

                    session['logged_in'] = True
                    session['username'] = login_query.username
                    session['email'] = login_query.email

                    msg = "Login Successful"
                    #redirect to index page
                    #return redirect(url_for('index'))
                    render_template("user-login.html",msg=msg)
                else:
                    #log password failure
                    current_app.logger.info("Password doesn't match")
                    #error 'Invalid password'
                    error = "Invalid Username or Password"
                    return render_template("user-login.html",error=error)
            else:
                #log username not found
                current_app.logger.info("Username not found")
                #error 'Username not found'
                error = "Username not found"
                return render_template("user-login.html",error=error)
        else:
            #log invalid data input
            current_app.logger.info("Failed to pass input requirements criteria")

            #error
            error = "Invalid or null data input"
            return render_template("user-login.html",error=error)
    #if method not post render template
    return render_template("user-login.html")

        
    
