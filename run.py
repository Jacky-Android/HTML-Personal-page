import json
from flask import Flask, render_template
import time

import os
from flask import send_from_directory
app = Flask(__name__)

@app.route("/")

def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    
    app.run('172.16.83.215')#172.16.83.215