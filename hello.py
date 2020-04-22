from flask import Flask, request, g, session, abort, redirect
from flask.helpers import make_response

app = Flask(__name__)


@app.route('/index')
def index():
    return '<h1>Hello World</h1>'


@app.route('/usr/<int:id>')
def usr(id):
    return f'<h1>Hello Usr {id}</h1>'


@app.route('/urlMap')
def urlMap():
    li = []
    for rule in app.url_map.iter_rules():
        li.append(f'<li>{rule.rule}: {rule.endpoint}</li>')
    lis = ''.join(li)
    return f'<ul>{lis}</ul>'


@app.route('/notfound')
def notfound():
    abort(418)
    return '<h1>Not return</h1>'


@app.route('/redirect')
def redirect_url():
    return redirect('/hole', code=307)


@app.route('/tuple')
def tuple_return():
    return '<h1>Tuple return with 202</h1>', 202


@app.route('/hole')
def hole():
    response = make_response(
        '<h1>Response object to Hole with cookie</h1><p id=\'x\'>loading</p><script>setTimeout(function() {document.getElementById(\'x\').textContent = document.cookie;},4000)</script>')
    response.set_cookie('answer', '42')
    return response


if __name__ == '__main__':
    app.run()
