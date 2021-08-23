# 9.4.3 Import the Flask dependency
from flask import Flask

# Create a new Flask App Instance
app = Flask(__name__)

# Create a Flask route
@app.route('/')
def hello_world():
    return 'Hello world'