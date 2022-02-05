from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def query_example():

    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)

if __name__ == '__main__':
    app.run(host='192.168.0.171', port=2000)
