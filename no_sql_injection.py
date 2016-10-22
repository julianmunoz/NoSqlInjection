import ast
from flask import Flask
from flask import render_template
from pymongo import MongoClient
from flask import request


app = Flask(__name__)
connection = MongoClient()
db = connection['login_database']
collection = db['login_collection']


@app.route('/login')
def render_login():
    return render_template('index.html')


def render_search_with_data(info):
    return render_template('user_info.html', user_list=info)


@app.route('/search')
def render_search():
    return render_template('user_info.html')


def render_search_error():
    return render_template("search_error.html")


def render_login_suc():
    return render_template("login_suc.html")


def render_login_error():
    return render_template("login_error.html")


@app.route("/login", methods=['POST'])
def process_post():
    user = request.form.get('u')
    passwd = request.form.get('p')
    where = {"$where": "this.password == '"+passwd+"'"}
    data = collection.find(where)
    for elem in data:
        if elem['user'] == user and elem['password'] == passwd:
            return render_login_suc()
    return render_login_error()


@app.route("/search", methods=['POST'])
def process_post_for_search():
    user_data = []
    user = request.form.get('u')
    if "{" in user:
        user = ast.literal_eval(user)
    data = collection.find({"user": user})
    for elem in data:
        user_data.append(elem["user"])
        try:
            user_data.append(elem["email"])
        except:
            continue
    if user_data:
        return render_search_with_data(user_data)
    return render_search_error()


if __name__ == '__main__':
    app.run(host="0.0.0.0")

#{"$gt": ""}