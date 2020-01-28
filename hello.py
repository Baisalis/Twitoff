from flask import Flask

app = Flask(__name__)

@app.route('/user')
def root():
  return("<h2> Hello World! </h2>")
    