from flask import Blueprint, render_template, redirect

from model import schedule

blue = Blueprint('schedule', __name__, static_folder='static', template_folder='templates')


@blue.route('/<id_schedule>')
def grade(id_schedule: str):
    id_schedule = int(id_schedule)
    returned_schedule = schedule.find_one({'id_schedule': id_schedule})
    print(returned_schedule)
    if returned_schedule is None:
        return redirect('/')
    return render_template('grade.html', schedule=returned_schedule.__dict__)


@blue.route('/api/<id_schedule>')
def api_grade(id_schedule: int):
    id_schedule = int(id_schedule)
    returned_schedule = schedule.find_one({'id_schedule': id_schedule})
    if returned_schedule is None:
        return redirect('/')
    return returned_schedule.__dict__
