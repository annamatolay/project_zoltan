"""
Created by Matolay Pál
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chapter/<chapter_number>")
def chapter(chapter_number):
    return render_template("/chapter.html", chapter=chapter_number)


if __name__ == "__main__":
    app.run(debug=True)
