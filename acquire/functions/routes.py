import re

#validate firstname
def validate_name(name):
    if re.search("^[a-zA-Z\'\. \-]{2,30}$",name):
        #validation success
        return name
    return 1

#validate email
def validate_email(email):
    if re.search("^[a-zA-Z0-9.\%-_]+\@[a-zA-Z0-9_.-]+\.[a-zA-Z]{2,5}$",email):
        return email
    return 1

#validate password
def password_validate(password):
    if re.search("^(?=[-_a-zA-Z0-9]*?[A-Z])(?=[-_a-zA-Z0-9]*?[a-z])(?=[-_a-zA-Z0-9]*?[0-9])\S{8,}$",password):
        return password
    return 1

#check password is same
def password_match(password,confirm):
    if password_validate(password) is not 1:
        if password == confirm:
            return password
    return 1

#username validation
def username_validation(username):
    if re.search("^(?=[-_a-zA-Z0-9]*?[A-Z])(?=[-_a-zA-Z0-9]*?[a-z])(?=[-_a-zA-Z0-9]*?[0-9])\S{8,}$",username):
        return username
    return 1

