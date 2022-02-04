from flask import Flask


app = Flask(__name__)


@app.route('/<info>')
def receive(info):
    if info == 'image':
        return open('screen.png', 'rb').read()


if __name__ == '__main__':
    app.run()
