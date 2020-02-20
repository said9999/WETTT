from flask import Flask, escape, request, redirect

app = Flask(__name__, static_folder='../web', static_url_path='')

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return redirect('/index.html', code=302) 
