from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)

@app.route('/')
def index():

    params = {
        'q': query,
        'key': 'DT7VKCNIRM18',
        'limit': '10'}
    r = requests.get("https://api.tenor.com/v1/search", params=params)
    gifJson = r.json()




    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
