from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    with open('/path/to/ping_results.txt', 'r') as f:
        data = f.readlines()
    return "<br>".join(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)