from flask import Flask, request, g, session, abort, redirect, render_template
from flask.helpers import make_response

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard_to_guess_string'

bootstrap = Bootstrap(app)
mmt = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/usr/<name>')
def usr(name):
    mock_list = ['Apple', 'Pineapple', 'Pen', 'Pencil']
    return render_template('user.html', name=name, list=mock_list)


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
        render_template('hole.html'))
    response.set_cookie('answer', '42')
    return response

# Error handling
@app.errorhandler(418)
def im_a_teapot(e):
    return render_template('418.html'), 418


class NameForm(FlaskForm):
    name = StringField("What's your name?", validator=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run()
