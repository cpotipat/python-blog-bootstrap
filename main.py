from flask import Flask, render_template, request
import requests

all_posts = requests.get("https://api.npoint.io/3ab6bac1c6a5832a27c6").json()


app = Flask(__name__)


@app.route("/")
def get_all_post():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/form-entry", methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone_number = request.form["phone"]
    message = request.form["message"]
    return f"<h1>Thanks {name}! We successfully sent your message.</h1>"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in all_posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
