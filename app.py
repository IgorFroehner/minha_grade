from flask import Flask, render_template
from decouple import config
from mongoengine import connect
from model import Schedule

import blueprints

app = Flask(__name__)
app.register_blueprint(blueprints.schedule_controller, url_prefix='/schedule')

connect(host=f"mongodb+srv://{config('DB_USER')}:{config('DB_PASS')}@cluster0.ogn2b.mongodb.net/myFirstDatabase"
             f"?retryWrites=true&w=majority")


@app.route('/')
def index() -> str:
    schedules = Schedule.objects
    print(schedules)
    return render_template('index.html', schedules=schedules)


@app.route('/minha_grade')
def minha_grade():
    return render_template('minha_grade.html')


if __name__ == '__main__':
    app.run(debug=True)
