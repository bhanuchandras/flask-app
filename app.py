from flask import Flask
from datetime import datetime
import os
# datetime object containing current date and time
 
app = Flask(__name__)

@app.route('/')
def hello_docker():
    now = datetime.now()
    return '<h1>Hello from Flask & Docker</h2> <p> Today date and Time is '+now.strftime("%d/%m/%Y %H:%M:%S")+'</p>'+'<br>'+os.uname()[1]

if __name__ == "__main__":
    app.run(debug=True)
