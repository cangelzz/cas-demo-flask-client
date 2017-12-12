from flask import Flask, render_template
from flask_cas import CAS, login_required

app = Flask(__name__)
cas = CAS()
cas.init_app(app)
app.config["CAS_SERVER"] = "http://www.casdemo.com:8000"
app.config["CAS_LOGIN_ROUTE"] = "/cas/login"
app.config["CA_LOGOUT_ROUTE"] = "/cas/logout"
app.config['CAS_AFTER_LOGIN'] = 'route_root'

app.secret_key = "daac6c368a3141ff9104b3b1e7c6c24d"

@app.route("/")
@login_required
def index():
    return render_template('index.html', username=cas.username, cas=cas)

@app.route("/protected/")
@login_required
def protected():
    return render_template('index.html', username = cas.username, cas=cas)

if __name__ == '__main__':
    app.run()