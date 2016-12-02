#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by Matolay Pál
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sekcio/<section_number>")
def section(section_number):
    return render_template("/section.html", section=section_number)


if __name__ == "__main__":
    app.run()
