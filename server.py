from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page/<page_number>")
def page(page_number):
    return render_template("/page.html", page=page_number)


if __name__ == "__main__":
    app.run(debug=True)
