from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
   return 'Hello World, Excited to see my App in a Docker container!'


if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)