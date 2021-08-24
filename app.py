from flask import Flask, render_template, flash, redirect
from decouple import config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from hashlib import sha256


app = Flask(__name__)
login_manager = LoginManager()


def config_app(_app):
    db_pass = config('MONGO_PASS')
    db_user = config('MONGO_USER')
    _app.config['SECRET_KEY'] = config('SECRET_KEY')
    _app.config['MONGODB_SETTINGS'] = {
        'host': f'mongodb+srv://{db_user}:{db_pass}@cluster0.ogn2b.mongodb.net/my_schedule?retryWrites=true&w=majority'
    }
    _db = MongoEngine(app)
    return _app, _db


def register_routes(_app):
    from routes import blueprints
    for blueprint in blueprints:
        _app.register_blueprint(blueprint)
    return _app


app, db = config_app(app)
app = register_routes(app)
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user):
    from model import User
    return User.objects.get(user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    from model.user_dao import LoginForm
    from model import user_dao

    form = LoginForm()
    if form.validate_on_submit():
        user = user_dao.find_by_user(form.user.data)
        if user is not None:
            if user.password == sha256(form.password.data.encode('utf-8')).hexdigest():
                flash('Logged in Successfully.')
                user.authenticated = True
                login_user(user)
                return redirect('/')
        else:
            return render_template('login.html', form=form, erro='Email ou senha incorretos')
    return render_template('login.html', form=form, title='Login')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/')
def index() -> str:
    return render_template('index.html', title='Home')


@app.route('/my_schedule')
def minha_grade():
    return render_template('my_schedule.html', title='Minha Grade')


if __name__ == '__main__':
    app.run(debug=True)
