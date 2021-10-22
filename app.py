from flask import Flask, jsonify, render_template, request, Response
import json
import pandas as pd

app = Flask(__name__)
app._static_folder = "D:\Website\static"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
   #app.run(debug = True)
   app.run(debug = True, host = '0.0.0.0', port = '8050')