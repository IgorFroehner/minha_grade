from flask import Flask, render_template
from model import schedule

import blueprints

app = Flask(__name__)
app.register_blueprint(blueprints.schedule_controller, url_prefix='/schedule')


@app.route('/')
def index() -> str:
    schedules = schedule.find_all()
    print(schedules)
    return render_template('index.html', schedules=schedules)


@app.route('/minha_grade')
def minha_grade():
    return render_template('minha_grade.html')


if __name__ == '__main__':
    app.run(debug=True)
