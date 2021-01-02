# Flask#2-Template

## Ninja2 Template engine

### Render template in view function

**Ref:** https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates

Flask will look for **templates** in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

`return render_template('user.html', value=value)`

### Usage

```
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}. </p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```

#### Filtering
`Hello, {{ name|capitalize }}`
- capitalize: First letter upper, rest lower
- upper
- lower
- title: title case
- trim: remove trailing space
- safe: without escaping letters, `dangerouslySetInnerHTML`, by default `<h1>` will be escaped to `&lt;h1&gt;`
- scriptags: remove all html tag from string

#### If:
```
{% if user %}
      Hello, {{ user }}!
  {% else %}
      Hello, Stranger!
{% endif %}
```

#### Macro:
- function in template
```
{% macro render_comment(comment) %} 
  <p>{{ comment }}</p>
{% endmacro %}

{{ render_comment(comment) }}
```

#### Loop and import:
- use function in template
```
{% import 'macros.html' as macros %}

<ul>
    {% for comment in comments %}
        {{ macros.render_comment(comment) }}
    {% endfor %}
</ul>
```

#### include:
- copy paste html
```
{% include 'common.html' %}
```

#### block:
- extendable template base/block
- call `{{ super() }}` to preserve block content in `base.html`
```
<head>
    {% block head %}
    <title>
        {% block title %}{% endblock %} - My Application
    </title>
    {% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

```
{% extends "base.html" %}

{% block title %}
    Index
{% endblock %}

{% block head %}
    {{ super() }}
    <style>
        * {
            box-sizing: border-box;
        }
    </style>
{% endblock %}

{% block body %}
    <h1>Hello, World!</h1>
{% endblock %}
```

### UI library (Bootstrap)
Install package:
`$ pip install flask-bootstrap`

Configure to flask app:
```py
from flask_bootstrap import Bootstrap 
# ...

# init bootstrap templates to extend in app
bootstrap = Bootstrap(app)
```

Use in template:
```
{% extends 'bootstrap/base.html' %}
{% block content %}
<div class="contianer">
  <p>Hello, {{ name }}</p>
</div>
{% endblock content %}
{% block styles %}
  {{ super() }}
  <style>
  .my-title {
    color: red;
  }
  </style>
{% endblock styles %}
```

### template built-in func `url_for()`
`{{ url_for('static', filename='favicon.ico', _external = True) }}`

- It will get the url from function name, with kwargs as url params
- `_external = True` will compile the absolute path/url

### External script (Moment)
Install package:
`$ pip install flask-moment`

Configure to flask app:
```py
from flask_moment import Moment 
# ...

# init bootstrap templates to extend in app
mmt = Moment(app)
```

Use in template:
- In template: moment will generate a JS script (pure magical JQuery code)

```
{% block scripts %}
  {{ super() }}
  {{ moment.include_moment() }}
  {{ moment.locale('zh-CN') }}
{% endblock %}

<p>The local date and time is {{ moment(current_time).format('LLL') }}. </p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
```

### Misc
- `@app.errorhandler(404)`
- Folders `/templates` for templates, `/static` for static files
