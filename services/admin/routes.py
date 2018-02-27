from flask import Blueprint,render_template

mod = Blueprint('admin',__name__,template_folder="templates")

@mod.route("/")
def authentication():
    return render_template("admin/index.html")