from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "df13160fbda91cc4881447f3d887dd12"

posts = [
    {
        "title": "Blog Post 1",
        "author": "Aditya",
        "time": "Jan 17 2020",
        "content": "This is the first post"
    },
    {
        "title": "Blog Post 2",
        "author": "adshin21",
        "date_posted": "Jan 18 2020",
        "content": "This is the second post"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    print("*" * 100)
    print(form)
    redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
