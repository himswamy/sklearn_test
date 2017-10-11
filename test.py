from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
   return 'Hello World, azure python!'


if __name__ == '__main__':
   app.run()
