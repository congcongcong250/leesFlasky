# Flask#3-WebForm

## WTForms
`pip install flask-wtf`

> Unlike most other extensions, Flask-WTF does not need to be initialized at the application level, but it expects the application to have a secret key configured.

```py
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
```

## CSRF

> Flask-WTF requires a secret key to be configured in the application because this key is part of the mechanism the extension uses to protect all forms against cross-site request forgery (CSRF) attacks.

We could also using auth, or recaptcha to prevent it.