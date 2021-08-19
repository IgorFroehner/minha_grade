from flask import Blueprint, render_template, redirect

from model import Schedule

blue = Blueprint('schedule', __name__, static_folder='static', template_folder='templates')


@blue.route('/<id_schedule>')
def grade(id_schedule: str):
    id_schedule = int(id_schedule)
    returned_schedule = Schedule.objects.get(id_schedule=id_schedule)
    print(type(returned_schedule))
    if returned_schedule is None:
        return redirect('/')
    return render_template('grade.html', schedule=returned_schedule)


@blue.route('/api/<id_schedule>')
def api_grade(id_schedule: int):
    id_schedule = int(id_schedule)
    returned_schedule = Schedule.objects.get(id_schedule=id_schedule)
    if returned_schedule is None:
        return redirect('/')
    return returned_schedule.__dict__
