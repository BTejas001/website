from flask import Flask, redirect, url_for, render_template

myweb = Flask(__name__)

@myweb.route("/")
@myweb.route("/home")
def home():
    return render_template("home.html", title = "Home")


@myweb.route("/about")
def about():
    return render_template("about.html", title = "About")


@myweb.route("/projects")
def projects():
    return render_template("projects.html", title = "Projects")


@myweb.route("/contact")
def contact():
    return render_template("contact.html", title = "Contact")


if __name__ == "__main__":
    myweb.run(debug=True)