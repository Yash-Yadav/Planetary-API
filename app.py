from flask import Flask, jsonify

app = Flask(__name__)

# Routes
@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/demo')
def hello_demo():
  return jsonify(message = 'Hello DEMO!')

if __name__ == '__main__':
  app.run(debug=True) 