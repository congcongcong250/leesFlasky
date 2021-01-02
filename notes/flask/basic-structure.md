# Flask#1-basic-structure

## Virtual Environment

`venv` (for Python 3) and virtualenv (for Python 2) allow you to manage separate package installations for different projects.

### local pkg mgmt

- Create

`> python -m venv VIRTUAL_ENV_NAME`

will create a virtual env with a local interpreter in CURRENT folder under folder name `VIRTUAL_ENV_NAME`

`-m` run module as a script, `venv` is a module

- Activate

`> source VIRTUAL_ENV_NAME/bin/activate`

This will change python PATH, remember to deactivate

## pip

`> pip install PKG_NAME`

`> pip freeze` to list all the local pkg

## Flask app

- Start
```py
from flask import Flask

app = Flask(__name__)
```
- Routing
```py
# #1
# type of param to match: int, float, string, path, uuid
@app.route('/user/<int:id>') 
def user(id):
	return '<h1>{}</h1>'.format(id) # python string format
	
# #2 
# Used internally in app.route() decorator
app.add_url_route('/','index',index_func)
```

param types work as a filter, only path applies to filter will fall into view func

url filter matching ordered top-down

- Run flask server

1. `> FLASK_APP=entry.py flask run`
2. `app.run()` programmatically

- Run flask debug server
A web based tool to debug only on browser, enable debugger and reloader

1. `>FLASK_DEBUG=1 FLASK_APP=entry.py flask run`
2. `app.run(debug=true)` pragrammatically

- Request and Response
`from flask import request`
Flask context globals:
1. `current_app` in Application context
2. `g` to store shared data in Application context, **reset with each request**
4. `request` in Request context
3. `session` in Request context

- Application context

```py
app_ctx = app.app_context()
app_ctx.push()
# current_app accessible
app_ctx.pop()
```

- `app.url_map`
A object contains the url map, iterate by `app.url_map.iter_rules()`

- Request
1. `values` dict combining the values in `form` and `args`, if any.
2. `get_data()`: buffered data; `get_json()`: parsed json
3. `scheme`: http or https; `is_secure()`: True if https
4. `before_first_request`, `before_request`, `after_request`, `teardown_request`: teardown is for exception thrown

- Response
1. `abort(418)` throw exception and return error response
2. `return redirect('/hole', code=307)` gives redirect response
3. `return '<h1>Tuple return with 202</h1>', 202`, return tuple for response
4. `response = make_response(HTML) return response` make complex response