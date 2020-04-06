from flask import Flask, escape, request, redirect

app = Flask(__name__, static_folder='../web', static_url_path='')

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return redirect('/index.html', code=302) 

@app.route('/restaurants/random')
def random():
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/
    # todo
    # get dao
    # dao.get_random_choice()
    # dao.get_ads()
    # combine result
    pass