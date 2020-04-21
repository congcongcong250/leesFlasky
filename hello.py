from flask import Flask, request, g, session
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


if __name__ == '__main__':
    app.run()
