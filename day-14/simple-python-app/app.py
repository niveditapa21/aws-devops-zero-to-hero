from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world this is India the super power!'

if __name__ == '__main__':
    app.run()

