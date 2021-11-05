from flask import Flask, render_template
import flask_ngrok

ngrok = flask_ngrok
app = Flask(__name__)
ngrok.run_with_ngrok(app)


@app.route("/")
def index():
    name = " ".join(
        [value[0] + len(value[1:]) * '*' for value in "Иванов Дмитрий Александрович".split()])
    number = "9760 0000 4032 4333"
    happy_birthday = "23.09.2003"
    sellby = "03.08.2022"
    passport = "78** ***283"
    return render_template("index.html", name=name, number=number, happy_birthday=happy_birthday,
                           sellby=sellby, passport=passport)


def url():
    return ngrok._run_ngrok()


def run():
    app.run()
