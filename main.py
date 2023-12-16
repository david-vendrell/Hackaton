from flask import Flask, request, send_file, redirect, jsonify, json, current_app
from controller import Controller
import pytz
import json
import threading


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/', methods=['POST'])
def test_request():
    try:
        type = request.json[""]
        content = request.json[""]
        Controller().handle_request(type, content)
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    print("Starting server...")
    app.run(host='127.0.0.1', port=8080, debug=True)