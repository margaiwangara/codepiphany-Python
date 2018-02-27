from flask import Blueprint,render_template

mod = Blueprint('fast-exec',__name__,template_folder="templates")

@mod.route("/")
def index():
    return render_template("index.html")

@mod.route("/about")
def about_us():
    return render_template("index.html")
@mod.route("/videos")
def videos():
    return render_template("index.html")