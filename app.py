from flask import Flask, render_template, json, request, redirect, url_for, jsonify

import datetime
import os
import base64
from time import time
import tempfile

app = Flask(__name__)

userID = 'none'
password = 'none'

@app.route('/about',  methods=['GET', 'POST'])
def about():

    return render_template('ShellLearn_About.html')

@app.route("/")
def main():

    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            userID = request.form['username']
            password = request.form['password']
            return redirect(url_for('about'))
    return render_template('login.html', error=error)

@app.route('/ShellLearn_book', methods=['GET', 'POST'])
def level1ABC():
    # if userID != 'none' :

        return render_template('ShellLearn_book.html')
    # else:
    #    return render_template('login.html') 

@app.route('/home',  methods=['GET', 'POST'])
def home():

    return render_template('index.html')

TMP_DIR_NAME = 'Images'

@app.route("/save-as-base64/", methods=['POST'])
def base64_saver():
    filename = '{:10d}.png'.format(int(time()))  # generate some filename
    filepath = os.path.join(TMP_DIR_NAME, filename)
    with open(filepath, "wb") as fh:
        base64_data = request.json['image'].replace('data:image/png;base64,', '')
        fh.write(base64.b64decode(base64_data))

    return jsonify({})


if __name__ == "__main__":
    app.run()